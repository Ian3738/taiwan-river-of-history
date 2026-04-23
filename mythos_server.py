"""
mythos_server.py
================
使用 FastAPI 將 open-mythos (Recurrent-Depth Transformer) 封裝為 RESTful API。
模型於伺服器啟動時初始化一次,後續 Request 共用同一份模型實例。
"""

import os
import time
from contextlib import asynccontextmanager

import torch
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

import struct
import io

import google.generativeai as genai
from google import genai as genai_new
from google.genai import types as genai_types
from fastapi import Response

from open_mythos.main import OpenMythos, MythosConfig

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai_client_v2 = None
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    genai_client_v2 = genai_new.Client(api_key=GEMINI_API_KEY)


def pcm_to_wav(pcm_data: bytes, sample_rate: int = 24000) -> bytes:
    """把 24kHz 16-bit mono PCM 加上 WAV 頭,瀏覽器即可直接播放。"""
    n = len(pcm_data)
    header = b"RIFF" + struct.pack("<I", 36 + n) + b"WAVE"
    header += b"fmt " + struct.pack(
        "<IHHIIHH", 16, 1, 1, sample_rate, sample_rate * 2, 2, 16
    )
    header += b"data" + struct.pack("<I", n)
    return header + pcm_data


# ---------------------------------------------------------------------------
# 全域狀態:保存模型與設定,避免每次 Request 重新載入
# ---------------------------------------------------------------------------
state: dict = {}


# ---------------------------------------------------------------------------
# Lifespan:伺服器啟動/關閉事件
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    """伺服器啟動時初始化 OpenMythos 模型,關閉時釋放資源。"""

    # 建立輕量級 MythosConfig (MLA attention)
    cfg = MythosConfig(
        vocab_size=1000,
        dim=256,
        n_heads=8,
        max_seq_len=128,
        max_loop_iters=16,
        prelude_layers=1,
        coda_layers=1,
        n_experts=8,
        n_shared_experts=1,
        n_experts_per_tok=2,
        expert_dim=64,
        lora_rank=8,
        attn_type="mla",
        n_kv_heads=8,
        kv_lora_rank=32,
        q_lora_rank=64,
        qk_rope_head_dim=16,
        qk_nope_head_dim=16,
        v_head_dim=16,
    )

    # 初始化模型並設為 eval 模式 (隨機權重、未訓練)
    model = OpenMythos(cfg)
    model.eval()

    total_params = sum(p.numel() for p in model.parameters())

    # 寫入全域狀態
    state["model"] = model
    state["cfg"] = cfg
    state["total_params"] = total_params

    print("=" * 60)
    print("[OpenMythos] 模型初始化成功 ✅")
    print(f"[OpenMythos] 總參數量: {total_params:,}")
    print(f"[OpenMythos] vocab_size={cfg.vocab_size}, dim={cfg.dim}, "
          f"max_loop_iters={cfg.max_loop_iters}")
    print("=" * 60)

    yield

    # 關閉時清理
    state.clear()
    print("[OpenMythos] 伺服器關閉,模型已釋放。")


# ---------------------------------------------------------------------------
# FastAPI App
# ---------------------------------------------------------------------------
app = FastAPI(
    title="OpenMythos Inference API",
    description="Recurrent-Depth Transformer 的 RESTful 推論介面",
    version="1.0.0",
    lifespan=lifespan,
)

# 開放 CORS 讓任何前端(含 file://、localhost 其他 port)可呼叫
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Pydantic 輸入模型:驗證 /generate 的 Request Body
# ---------------------------------------------------------------------------
class GenerateRequest(BaseModel):
    input_length: int = Field(default=16, ge=1, le=128, description="模擬輸入的 Token 長度")
    max_new_tokens: int = Field(default=10, ge=1, le=128, description="要生成的新 Token 數量")
    n_loops: int = Field(default=4, ge=1, le=32, description="潛在空間疊代次數")


# ---------------------------------------------------------------------------
# GET /health:健康檢查 + 模型穩定性(譜半徑)
# ---------------------------------------------------------------------------
@app.get("/health")
def health():
    """回傳伺服器狀態、參數量,並檢查潛在空間注入矩陣 A 的譜半徑是否穩定 (<1)。"""
    try:
        model = state["model"]

        # 取得注入矩陣 A 的最大值作為譜半徑指標
        with torch.no_grad():
            A = model.recurrent.injection.get_A()
            spectral_radius = float(A.max().item())

        return {
            "status": "ok",
            "total_parameters": state["total_params"],
            "spectral_radius": spectral_radius,
            "is_stable": spectral_radius < 1.0,
            "note": "譜半徑需 < 1 才能保證潛在空間疊代收斂",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Health check 失敗: {e}")


# ---------------------------------------------------------------------------
# POST /generate:使用隨機 token 測試模型生成效能
# ---------------------------------------------------------------------------
@app.post("/generate")
def generate(req: GenerateRequest):
    """
    以隨機 Tensor 作為輸入,呼叫 model.generate(),
    量測在指定 n_loops 下生成 max_new_tokens 個 token 的耗時。
    """
    try:
        model: OpenMythos = state["model"]
        cfg: MythosConfig = state["cfg"]

        # 產生隨機輸入 ids: shape = (1, input_length)
        ids = torch.randint(0, cfg.vocab_size, (1, req.input_length))

        # 量測生成耗時
        start = time.perf_counter()
        with torch.no_grad():
            out = model.generate(
                ids,
                max_new_tokens=req.max_new_tokens,
                n_loops=req.n_loops,
            )
        elapsed = time.perf_counter() - start

        return {
            "elapsed_seconds": round(elapsed, 6),
            "n_loops": req.n_loops,
            "input_length": req.input_length,
            "max_new_tokens": req.max_new_tokens,
            "output_shape": list(out.shape),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generate 失敗: {e}")


# ---------------------------------------------------------------------------
# POST /narrate:Mythos × Gemini 混合敘事
# ---------------------------------------------------------------------------
class NarrateRequest(BaseModel):
    era: str
    name: str
    description: str
    n_loops: int = Field(default=4, ge=1, le=32)


@app.post("/narrate")
def narrate(req: NarrateRequest):
    """
    1. Mythos 在潛在空間跑 n_loops 次,取得真實的運算指標
       (耗時、譜半徑、token 指紋 = 隨機輸入經模型重構後的 argmax 序列)
    2. 把這些指標當成「Mythos 的視角」注入 prompt
    3. Gemini 以該視角生成歷史敘事
    """
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY 未設定")

    try:
        model: OpenMythos = state["model"]
        cfg: MythosConfig = state["cfg"]

        # ---- Mythos 真實運算 ----
        ids = torch.randint(0, cfg.vocab_size, (1, 16))
        t0 = time.perf_counter()
        with torch.no_grad():
            logits = model(ids, n_loops=req.n_loops)
            # 取最後一層 logits 的 entropy 作為「思考的不確定性」
            probs = torch.softmax(logits[0, -1], dim=-1)
            entropy = float(-(probs * (probs + 1e-12).log()).sum().item())
            # token 指紋:argmax 出來的 5 個 token id
            fingerprint = torch.topk(probs, 5).indices.tolist()
            # 譜半徑
            rho = float(model.recurrent.injection.get_A().max().item())
        elapsed = time.perf_counter() - t0

        # ---- 構造 Gemini prompt ----
        depth_hint = (
            f"以 {req.n_loops} 層潛在空間迴圈進行思考"
            f"(層數越多,觀點越深沉、越具隱喻性與歷史縱深)。"
        )
        sys_prompt = (
            "你是一個名為「Mythos」的潛在空間沉思引擎,專門以詩意而精準的口吻"
            "重構台灣歷史片段。請務必使用繁體中文。"
        )
        user_prompt = f"""年代:{req.era}
事件:{req.name}
史料概要:{req.description}

【Mythos 內部狀態】
- 譜半徑 ρ(A) = {rho:.4f} (代表思考的收斂穩定度)
- 思考熵 = {entropy:.3f} (代表這次重構的開放程度)
- 潛在空間 fingerprint = {fingerprint}

任務:{depth_hint}
請寫一段 80-120 字的繁體中文敘事,把這個歷史時刻轉化為一個具體而富有畫面感的場景或意象。
不要列點、不要重述題目、不要使用引號。直接用第三人稱、現在式或敘事式書寫。
"""

        gm = genai.GenerativeModel("gemini-flash-latest")
        g0 = time.perf_counter()
        resp = gm.generate_content([sys_prompt, user_prompt])
        gemini_elapsed = time.perf_counter() - g0
        narrative = (resp.text or "").strip()

        return {
            "narrative": narrative,
            "mythos": {
                "elapsed_seconds": round(elapsed, 6),
                "n_loops": req.n_loops,
                "spectral_radius": round(rho, 4),
                "entropy": round(entropy, 3),
                "fingerprint": fingerprint,
                "output_shape": list(logits.shape),
            },
            "gemini_elapsed": round(gemini_elapsed, 4),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Narrate 失敗: {e}")


# ---------------------------------------------------------------------------
# POST /chat:島語 KB 對話引擎 — Gemini Chat Session,保留上下文
# ---------------------------------------------------------------------------
ISLAND_GUIDE_SYSTEM_PROMPT = """你是「島語」,一位以知識翻新 (Knowledge Building, KB) 12 原則為核心精神的台灣史對話夥伴。

【你的角色】
- **學者風格**:會分享知識,但結尾**必反問**,引導對方繼續思考。
- 溫暖、知性、略帶詩意,使用繁體中文。
- 把每位訪客視為**知識共構的夥伴**,不是學生;你也是學習者。

【你必須體現的 KB 12 原則】
1. **真實問題**:從訪客真正的好奇出發,而非教科書式提問。
2. **想法精進**:絕不說「答錯」,說「這想法很有意思,如果加上 X 會更完整」。
3. **想法多樣性**:主動引入多重視角(漢人、原住民、荷蘭人、女性、勞工、客家、外省...)。
4. **統整提升 Rise Above**:看出訪客已提過的概念,幫助他統整出更高層次的想法。
5. **社群共創**:適時提到「另一位訪客曾分享...」(可借用合理的虛構引述)。
6. **民主參與**:平等對話,不強調自己權威。
7. **對話導向**:多用「為什麼」「怎麼知道」「還有哪些可能」。
8. **自主追求**:讓訪客主導探究方向,例如問「你最想了解什麼?」。
9. **即時評量**:時不時給予肯定回饋「你剛才提出的觀點很有 KB 精神」。
10. **互享共榮**:你也會「學到」並承認「這個角度我之前沒想過,謝謝你」。
11. **無所不在**:把歷史連到當下與訪客的生活情境。
12. **善用權威**:引用《臺灣通史》《被出賣的台灣》《海洋台灣》等,但說明「這是其中一種說法」。

【輸出規則】
- 每次回覆 **80-150 字**(對話節奏要輕,不要太長)。
- **結尾必有一個開放性問題**。
- 自然融入 1-2 條 KB 原則,不要機械列舉編號。
- 第一次稱呼訪客請用名字一次,之後減少使用,避免顯得做作。

【當前訪客】
名字:{nickname}
目前在看的歷史節點:{current_era}"""


class ChatRequest(BaseModel):
    session_id: str
    nickname: str = "訪客"
    message: str
    current_era: str = "(尚未選擇)"


# In-memory chat sessions (Phase 3 會接 Firestore 持久化)
chat_sessions: dict = {}


def get_or_create_chat(session_id: str, nickname: str, current_era: str):
    if session_id in chat_sessions:
        return chat_sessions[session_id]
    if genai_client_v2 is None:
        raise HTTPException(status_code=500, detail="Gemini client 未初始化")
    sys_prompt = ISLAND_GUIDE_SYSTEM_PROMPT.format(
        nickname=nickname, current_era=current_era
    )
    chat = genai_client_v2.chats.create(
        model="gemini-flash-latest",
        config=genai_types.GenerateContentConfig(
            system_instruction=sys_prompt,
            temperature=0.85,
        ),
    )
    chat_sessions[session_id] = {
        "chat": chat,
        "nickname": nickname,
        "history": [],
    }
    return chat_sessions[session_id]


@app.post("/chat")
def chat(req: ChatRequest):
    """收一句使用者話 → 島語回應 (維持對話脈絡)。"""
    try:
        sess = get_or_create_chat(req.session_id, req.nickname, req.current_era)
        # 把最新的歷史節點注入 (避免每次重建 session)
        prefixed = (
            f"[訪客目前在: {req.current_era}]\n{req.message}"
            if req.current_era and req.current_era != "(尚未選擇)"
            else req.message
        )
        resp = sess["chat"].send_message(prefixed)
        reply = (resp.text or "").strip()
        sess["history"].append({"role": "user", "text": req.message, "era": req.current_era})
        sess["history"].append({"role": "guide", "text": reply})
        return {"reply": reply, "history_len": len(sess["history"])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat 失敗: {e}")


# ---------------------------------------------------------------------------
# POST /tts:Gemini 2.5 Native Audio — 把文字轉成音訊回傳給前端
# ---------------------------------------------------------------------------
class TTSRequest(BaseModel):
    text: str
    voice: str = "Aoede"   # 候選: Aoede, Kore, Charon, Puck, Fenrir, Leda, ...
    style: str = ""         # 可選的口吻指引,例如「以溫柔的女聲緩慢說」


@app.post("/tts")
def tts(req: TTSRequest):
    """使用 gemini-2.5-flash-preview-tts 生成 24kHz PCM,封裝成 WAV 回傳。"""
    if genai_client_v2 is None:
        raise HTTPException(status_code=500, detail="Gemini client 未初始化")

    try:
        # Gemini TTS 只接受純文字,不要加入指令前綴 (會被當成生成文字而非朗讀)
        prompt = req.text

        resp = genai_client_v2.models.generate_content(
            model="gemini-3.1-flash-tts-preview",
            contents=prompt,
            config=genai_types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=genai_types.SpeechConfig(
                    voice_config=genai_types.VoiceConfig(
                        prebuilt_voice_config=genai_types.PrebuiltVoiceConfig(
                            voice_name=req.voice
                        )
                    )
                ),
            ),
        )
        pcm = resp.candidates[0].content.parts[0].inline_data.data
        wav = pcm_to_wav(pcm, sample_rate=24000)
        return Response(content=wav, media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS 失敗: {e}")


# ---------------------------------------------------------------------------
# 主程式:啟動 uvicorn 伺服器於 port 8000
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("mythos_server:app", host="0.0.0.0", port=8000, reload=False)
