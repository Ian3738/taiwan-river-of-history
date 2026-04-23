# 台灣歷史長河 · River of Formosa

> 一個由粒子凝聚而成的台灣史互動展覽 — 以「島語」AI 導覽員陪伴觀眾穿越六千年的島嶼記憶。

![preview](https://img.shields.io/badge/Three.js-r128-blueviolet) ![](https://img.shields.io/badge/Gemini-2.5%20%2F%203.1-green) ![](https://img.shields.io/badge/Mythos-Recurrent--Depth-orange) ![](https://img.shields.io/badge/Firebase-Firestore-yellow)

## 這是什麼

一個結合 **3D 粒子視覺化、語音 AI 對話、知識翻新原則** 的單頁網站。

12,000 顆粒子會在 14 個歷史節點(從南島語族到 AI 共創時代)之間變形,每個年代都有專屬的立體圖案 — 蒸汽火車、向日葵、玉山、神經網絡⋯。

「島語」是粒子凝聚而成的 AI 導覽員,使用者可以:
- 🎤 用語音呼喚她、跟她對話
- 🤚 用手勢瀏覽歷史節點(MediaPipe Hands)
- 📱 觸控、滑鼠、鍵盤多種輸入並存
- 💾 對話歷史自動同步到 Firebase

## 技術組合

| 層 | 技術 |
|---|---|
| 視覺 | Three.js + 自製 Shader(粒子變形 + warp 特效) |
| 動作 | @mediapipe/hands(食指追蹤、捏合、握拳) |
| 語音輸入 | Web Speech API(zh-TW) |
| 語音輸出 | Gemini 2.5/3.1 Native TTS(Aoede 聲音) |
| AI 對話 | Gemini Chat Session + KB 12 原則 system prompt |
| 潛在空間 | OpenMythos(Recurrent-Depth Transformer) |
| 後端 | FastAPI + Pydantic |
| 資料庫 | Firebase Auth(匿名) + Firestore |

## 知識翻新 (KB) 12 原則

島語的對話人格內建了 Knowledge Building 12 條原則,自然體現在每次回應裡:

1. 真實問題 — 從訪客真正的好奇出發
2. 想法精進 — 不說「答錯」,說「如果加上 X 會更完整」
3. 想法多樣性 — 主動引入多重視角(原住民、漢人、女性、勞工⋯)
4. 統整提升(Rise Above)
5. 社群共創
6. 民主參與
7. 對話導向
8. 自主追求
9. 即時評量
10. 互享共榮
11. 無所不在
12. 善用權威

## 本地啟動

### 1. 後端(Mythos + Gemini API)
```bash
# 安裝 OpenMythos 模型
git clone https://github.com/kyegomez/OpenMythos
pip install -e ./OpenMythos

# 安裝其他依賴
pip install -r requirements.txt

# 設定 Gemini API Key
cp .env.example .env
# 編輯 .env 填入你的 key (https://aistudio.google.com/app/apikey)

# 啟動 FastAPI 後端 (port 8000)
python mythos_server.py
```

### 2. 前端(靜態網站)
```bash
# 用 Python 內建 server (port 8080)
python3 -m http.server 8080
```

打開 http://localhost:8080/taiwan-river.html → 點任一處 → 跟著島語的引導開始。

### 3. (可選)Firebase
若要啟用對話雲端同步:
1. 到 https://console.firebase.google.com 建專案
2. 啟用 **Authentication > Anonymous**、**Firestore Database**
3. 把你的 `firebaseConfig` 換到 `taiwan-river.html` 裡的 `<script type="module">` 區塊

## 14 個歷史節點

| 年代 | 事件 | 粒子圖案 |
|---|---|---|
| ~4000 BCE | 南島語族的起源 | 🛶 獨木舟 + 海浪 |
| 1624 | 大航海的交會 | ⛵ 三桅大帆船 |
| 1661 | 鄭氏東寧的孤光 | 🏰 熱蘭遮城 |
| 1887 | 鐵路與電光之初 | 🚂 蒸汽火車 |
| 1895 | 乙未割讓的斷柱 | 斷柱 |
| 1921 | 文化覺醒的年代 | 📖 開書 + 燈泡 |
| 1947 | 二二八的裂縫 | 碎裂石碑 |
| 1980 | 矽島的崛起 | 💾 半導體晶圓 |
| 1987 | 解嚴後的綻放 | 🕊 破曉飛鳥 |
| 1996 | 首次總統直選 | 🗳 投票箱 |
| 1999 | 九二一的搖晃 | 🌋 山脈震波 |
| 2014 | 太陽花的春天 | 🌻 向日葵 |
| 2020 | 護國神山與口罩外交 | ⛰ 玉山 + 晶圓 |
| 2026 | AI 與共創時代 | 🧠 三層神經網絡 |

## 互動方式

| 方式 | 操作 |
|---|---|
| 🎤 語音 | 喚醒詞「島語」+ 命令(打開資訊卡 / 念給我聽 / 太陽花 / 開始探索⋯) |
| 🤚 手勢 | 食指移動、捏合(Mythos 重構)、握拳(回到長河)、雙手拉開(縮放) |
| 📱 觸控 | 左右滑切換年代、點選節點、雙指捏合 |
| 🖱 滑鼠 | 點時間軸、滾輪縮放 |
| ⌨️ 鍵盤 | ←→ 切換、Esc 回長河、1-9 跳轉年代 |

## 授權

MIT License — 歡迎自由使用、改作、再發行。

## 致謝

- [OpenMythos](https://github.com/kyegomez/OpenMythos) by Kye Gomez — Recurrent-Depth Transformer 模型
- [MediaPipe](https://developers.google.com/mediapipe) by Google — 手勢辨識
- [Gemini API](https://ai.google.dev/) by Google — 語音合成與對話引擎
- [Three.js](https://threejs.org/) — 3D 粒子渲染
- 知識翻新 (Knowledge Building) 原則 by Marlene Scardamalia & Carl Bereiter
