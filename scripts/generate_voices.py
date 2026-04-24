"""
批次生成 14 段歷史敘事的語音檔 + 常用島語對白。
使用 Gemini 3.1 Flash TTS 的 'Leda' 聲音(更自然女聲)。
生成一次後存到 voices/ 目錄,前端直接播放靜態檔,不再即時呼叫 Gemini。
"""

import os
import wave
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY missing — check .env")

client = genai.Client(api_key=API_KEY)

# 14 個歷史節點的敘事文字(與 index.html DATA 完全一致)
ERA_NARRATIVES = [
    ("era_bce4000", "距今約六千年前的史前台灣,具備農耕與精湛航海技術的先民,以台灣為起點,乘獨木舟展開跨越太平洋與印度洋的擴張,台灣被廣泛認定為「南島語族」的發源地,在人類海洋遷徙史上具備核心的歷史地位。"),
    ("era_1624",    "西元 1624 年荷蘭東印度公司於大員(今台南安平)建立熱蘭遮城,標誌著台灣正式捲入大航海時代的全球化貿易網,此時代的台灣成為東亞鹿皮、蔗糖等物資的國際轉運樞紐,並首次出現由羅馬拼音書寫的「新港文書」。"),
    ("era_1661",    "西元 1661 年鄭成功率軍擊退荷蘭政權,建立台灣史上首個漢人政權「東寧王國」,此階段的歷史重心在於軍隊屯田開墾與漢人典章制度的引入,全台首學的設立正式將儒家思想與傳統宗族文化深植於台灣社會。"),
    ("era_1887",    "西元 1887 年清法戰爭後台灣建省,首任巡撫劉銘傳啟動近代化建設,開始基隆至新竹鐵路的修築,以及電報線與電燈的架設,這是台灣從傳統農業社會步入近代工業化與基礎設施建設的啟蒙階段。"),
    ("era_1895",    "西元 1895 年甲午戰爭後《馬關條約》將台灣割讓予日本,引發台灣人民強烈的武裝抵抗(乙未戰爭),隨後展開的五十年日本殖民時期,總督府實行高壓統治與同化政策,同時也建立了現代化的戶政、公衛與水利等基礎設施。"),
    ("era_1921",    "西元 1921 年面對殖民體制,台灣知識份子林獻堂、蔣渭水等人成立「台灣文化協會」,歷史路線從武裝抗日轉向體制內的政治與文化啟蒙,透過發行報刊與舉辦講座,促成台灣現代公民意識與民族主體性的首次大規模覺醒。"),
    ("era_1947",    "西元 1947 年因戰後國民政府接管初期的施政失當與族群摩擦,爆發了全台性的「二二八事件」及隨後的武力鎮壓,這段沉痛的歷史造成大量本土菁英傷亡,並成為後續實施長達 38 年戒嚴與白色恐怖統治的開端。"),
    ("era_1980",    "西元 1980 年面對國際外交與經濟危機,台灣政府設立「新竹科學工業園區」,此時期歷史重點為經濟結構的重大轉型,藉由海外技術引進與人才回流,台灣開始發展半導體與資訊產業,奠定全球高科技代工重鎮的基礎。"),
    ("era_1987",    "西元 1987 年 7 月 15 日台灣正式解除長達 38 年的戒嚴令,黨禁與報禁的解除促使社會壓抑的能量全面釋放,各類社會運動蓬勃發展,政治反對勢力合法化,標誌著台灣正式邁入自由化與民主化的進程。"),
    ("era_1996",    "西元 1996 年台灣舉行史上首次總統直接選舉,儘管面臨第三次台海飛彈危機的外部軍事威嚇,大選依然順利完成,此歷史事件徹底落實了主權在民的民主原則,是台灣政治體制民主化完成的關鍵里程碑。"),
    ("era_1999",    "西元 1999 年 9 月 21 日台灣中部發生芮氏規模 7.3 強震,造成慘重傷亡與破壞,此事件的歷史意義不僅在於地理與社會的創傷,更在於災後展現的強大民間互助動能,促成國家級災難防救體系與建築防震法規的全面翻新。"),
    ("era_2014",    "西元 2014 年春季因反對立法院草率通過《海峽兩岸服務貿易協議》,爆發青年學生佔領立法院的「太陽花學運」,此時代背景反映了年輕世代對兩岸經貿過度依賴的疑慮,並深刻影響了隨後的政治版圖與公民參與模式。"),
    ("era_2020",    "西元 2020 年面對全球 COVID-19 疫情,台灣成功執行邊境管控並向國際輸出醫療物資,同時全球供應鏈的晶片短缺危機,讓國際社會強烈意識到台灣半導體產業在經濟與地緣政治上的戰略高度與不可替代性。"),
    ("era_2026",    "西元 2026 年生成式人工智慧全面普及,台灣憑藉先進製程晶片與強大的 AI 伺服器硬體生態系,成為全球算力網絡的核心支柱,此時期的歷史定位在於硬體製造與新興科技的深度融合,台灣持續以科技實力驅動全球的創新發展。"),
]

# 常用島語對白(靜態,可預生成)
COMMON_LINES = [
    ("line_wake",         "我在,請說。"),
    ("line_go",           "好的,我們出發。"),
    ("line_back_river",   "回到時間長河。"),
    ("line_card_open",    "資訊卡已展開。"),
    ("line_card_close",   "好的,關閉資訊卡。"),
    ("line_no_era",       "現在還沒有開啟任何年代,請先選一個。"),
    ("line_ask_name",     "你好,我是島語。在我們開始之前,你想讓我怎麼稱呼你?"),
    ("line_intro_1",      "你好,我是島語。"),
    ("line_intro_2",      "我會陪你穿越這座島嶼六千年的記憶,從南島語族的獨木舟,到 AI 與你共寫歷史的此刻。"),
    ("line_guide_self",   "我是島語,由粒子凝聚而成的你的 AI 導覽員。我專注於陪你深入探索台灣歷史。"),
]


VOICE_NAME = "Leda"   # 推薦的中文自然女聲
MODEL = "gemini-3.1-flash-tts-preview"
OUT_DIR = Path(__file__).resolve().parent.parent / "voices"
OUT_DIR.mkdir(exist_ok=True)


def tts_to_wav(text: str, out_path: Path, voice: str = VOICE_NAME, retries: int = 2):
    """呼叫 Gemini 生成 24kHz PCM 並存成 WAV。"""
    for attempt in range(retries + 1):
        try:
            resp = client.models.generate_content(
                model=MODEL,
                contents=text,
                config=types.GenerateContentConfig(
                    response_modalities=["AUDIO"],
                    speech_config=types.SpeechConfig(
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name=voice
                            )
                        )
                    ),
                ),
            )
            pcm = resp.candidates[0].content.parts[0].inline_data.data
            with wave.open(str(out_path), "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(24000)
                wf.writeframes(pcm)
            return True
        except Exception as e:
            print(f"  ⚠ attempt {attempt+1} failed: {e}")
            if attempt < retries:
                time.sleep(3)
    return False


def main():
    all_items = ERA_NARRATIVES + COMMON_LINES
    print(f"🎙 準備生成 {len(all_items)} 個語音檔到 {OUT_DIR}/")
    print(f"   聲音:{VOICE_NAME}  模型:{MODEL}\n")

    ok, skipped, failed = 0, 0, 0
    for slug, text in all_items:
        out = OUT_DIR / f"{slug}.wav"
        if out.exists():
            print(f"⏭  {slug}.wav 已存在,略過 (如要重新生成請先刪除)")
            skipped += 1
            continue
        print(f"🎵 {slug}:{text[:30]}…")
        success = tts_to_wav(text, out)
        if success:
            size_kb = out.stat().st_size / 1024
            print(f"   ✅ 儲存 {size_kb:.1f} KB\n")
            ok += 1
        else:
            print(f"   ❌ 失敗\n")
            failed += 1
        time.sleep(1.5)  # 避免 rate limit

    print(f"\n=== 完成 ===")
    print(f"✅ 新生成:{ok}  ⏭  略過:{skipped}  ❌ 失敗:{failed}")
    print(f"目錄:{OUT_DIR}")


if __name__ == "__main__":
    main()
