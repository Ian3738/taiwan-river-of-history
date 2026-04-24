# 🌊 台灣歷史長河 · River of Formosa

> 一座由粒子、聲音、對話與 AI 共構的**台灣史互動展覽** × **知識翻新 (KB) 諮商系統**。

<p align="center">
  <a href="https://ian3738.github.io/taiwan-river-of-history/">
    <img src="https://img.shields.io/badge/🌐_Live_Demo-ian3738.github.io-00e5ff?style=for-the-badge" />
  </a>
  <a href="https://huggingface.co/spaces/Ian3738/island-guide-server">
    <img src="https://img.shields.io/badge/🤗_Backend-HF_Space-e0a030?style=for-the-badge" />
  </a>
</p>

![](https://img.shields.io/badge/Three.js-r128-blueviolet) ![](https://img.shields.io/badge/Gemini-3.1_Flash_TTS-green) ![](https://img.shields.io/badge/Firebase-Auth+Firestore-FFCA28) ![](https://img.shields.io/badge/KB-12_Principles-orange) ![](https://img.shields.io/badge/License-MIT-blue)

---

## 🎯 這是什麼?

一個整合**多模態互動 + 生成式 AI + 學術研究框架**的單人(或小團隊)作品:

| 三個主要入口 | 連結 | 用途 |
|---|---|---|
| 🎨 **主展覽** | [`/`](https://ian3738.github.io/taiwan-river-of-history/) | 手勢 / 語音 / 觸控探索 14 個歷史節點的粒子視覺化 |
| 💭 **諮商室** | [`/counseling.html`](https://ian3738.github.io/taiwan-river-of-history/counseling.html) | 選一張歷史唱片,與「島語」AI 做 KB 式深度對話 |
| 📊 **語料分析後台** | [`/admin.html`](https://ian3738.github.io/taiwan-river-of-history/admin.html) | 管理員儀表板:描述統計、文字雲、N-gram、KB 原則偵測、APA 論文報告匯出 |

---

## ✨ 主要功能

### 🎨 主展覽
- **14 個歷史節點**,從 ~4000 BCE 南島語族到 2026 AI 時代
- **粒子 3D 視覺化**:每個年代有專屬的粒子立體圖案(蒸汽火車、太陽花、玉山...)
- **每個節點動態動畫**:海浪搖、地震、花瓣綻放、神經脈動等 10 種 shader-level 動畫
- **多模態互動**:
  - 🖐 手勢(MediaPipe Hands,食指撥動、捏合、握拳)
  - 🎤 語音(Web Speech + 喚醒詞「島語」+ 豐富年代關鍵字)
  - 📱 觸控(swipe 切換、pinch 縮放、tap 選取)
  - ⌨️ 鍵盤(←→、Esc、1-9)
- **島語 AI 導覽員**:
  - 使用 Gemini 3.1 Flash TTS 生成自然女聲
  - 以 KB 風格的詩意語調朗讀 14 段台灣史敘事
  - 可隨時喚醒、打斷、回應命令

### 💭 島語諮商室
- **唱片式介面**:復古琥棕色調,14 張歷史唱片橫向滑動選擇,懸停時黑膠從套中滑出旋轉
- **3 種對話模式**:年代專屬 / 自由對話 / 今日反思(隨機主題)
- **諮商級 UI**:1.08rem 襯線體、大間距、旋轉唱盤
- **語音 + 文字雙輸入**
- **KB 人格引擎**:system prompt 內嵌 Scardamalia & Bereiter 12 原則
- **Firebase 同步**:對話即時存雲端
- **匯出功能**:逐字稿 `.txt` + Gemini 生成的對話摘要

### 📊 語料分析後台
- **管理員登入**:Google OAuth + Firestore Security Rules 保護
- **描述性統計**:訊息長度直方圖、M/SD/Mdn/IQR、離散度分析
- **文字雲**:wordcloud2.js 渲染,可切換「使用者 vs 島語」
- **N-gram 分析**:高頻詞 Top 30、Bigram、Trigram
- **行為分析**:
  - 7×24 活躍熱圖
  - 提問比例 + Bloom's Taxonomy 分類(Why/How/Fact)
- **KB 原則偵測**:正則規則掃描島語回應,量化 12 原則出現頻率
- **日期篩選**:全部 / 今天 / 近 7/30/90 天 / 自訂範圍
- **📄 論文級報告生成**:
  - 自動生成 Methodology、Results、Discussion、Limitations 四段
  - 5 張 APA-7 風格表格(描述統計、年代參與度、KB 原則、N-gram、Bloom's 提問)
  - 匯出格式:Markdown / HTML (Word 直接開) / CSV (Excel/SPSS/R)
- **管理工具**:清空語料(兩階段確認)、匯出 CSV/JSON

---

## 🧠 知識翻新 (KB) 12 原則

島語的對話人格完全遵循 Scardamalia & Bereiter (2014) 的 KB 理論框架:

| # | 中文完整名 | 英文原名 |
|---|---|---|
| 1 | 從真實問題中瞭解真正的想法 | Real Ideas, Authentic Problems |
| 2 | 不斷精進的想法 | Improvable Ideas |
| 3 | 想法的多樣性 | Idea Diversity |
| 4 | 統整有助於想法昇華 | Rise Above |
| 5 | 知識為社群共創並負有共同責任 | Community Knowledge, Collective Responsibility |
| 6 | 知識創造為平等參與,成員的貢獻無法切割 | Democratizing Knowledge |
| 7 | 知識翻新注重對話 | Knowledge Building Discourse |
| 8 | 認知能動性 / 知識的自主追求者 | Epistemic Agency |
| 9 | 內嵌的、即時的、變革性的評量 | Embedded, Concurrent, and Transformative Assessment |
| 10 | 互享共榮的知識翻新過程 | Symmetric Knowledge Advancement |
| 11 | 無所不在的知識翻新 | Pervasive Knowledge Building |
| 12 | 建構性地運用權威資料 | Constructive Uses of Authoritative Sources |

---

## 📍 14 個歷史節點

| 年代 | 事件 | 粒子圖案 | Shader 動畫 |
|---|---|---|---|
| ~4000 BCE | 南島語族的起源 | 🛶 獨木舟 + 海浪 | 海浪搖擺 |
| 1624 | 大航海的交會 | ⛵ 三桅大帆船 + 熱蘭遮城 | 海浪搖擺 |
| 1661 | 鄭氏東寧的孤光 | 🏯 書院牌樓 + 鄭成功劍 | 靜態 |
| 1887 | 鐵路與電光之初 | 🚂 蒸汽火車 + 鐵軌 | 火車前進 + 煙飄 |
| 1895 | 乙未割讓的斷柱 | 🏛 斷柱 + 撕裂的馬關條約 | 斷裂顫抖 |
| 1921 | 文化覺醒的年代 | 📖 開書 + 燈泡 + 擴音器 | 煙霧上升 |
| 1947 | 二二八的裂縫 | 🕯 碎裂石碑 + 三根紀念燭台 | 熄滅閃爍 |
| 1980 | 矽島的崛起 | 💾 半導體晶圓 + die 矩陣 | 自轉 |
| 1987 | 解嚴後的綻放 | 🕊 破曉飛鳥 + 朝陽 | 飛升 |
| 1996 | 首次總統直選 | 🗳 投票箱 + 台灣島輪廓 | 靜態 |
| 1999 | 九二一的搖晃 | 🌋 山脈震波 | 雷動搖晃 (每 3 秒一次衰減) |
| 2014 | 太陽花的春天 | 🌻 向日葵 | 花瓣綻放呼吸 |
| 2020 | 護國神山與口罩外交 | ⛰ 玉山 + 晶圓 + 口罩 | 靜態 |
| 2026 | AI 與共創時代 | 🧠 三層神經網絡 | 脈動 |

---

## 🏗 技術架構

```
┌─────────────────────────────────────────────────────────┐
│  使用者瀏覽器                                            │
│  ├─ 前端三頁 (HTML/JS/CSS,無框架)                        │
│  ├─ MediaPipe Hands (手勢)                              │
│  ├─ Web Speech API (語音辨識)                           │
│  ├─ Three.js r128 (3D 粒子)                             │
│  └─ Firebase JS SDK (Auth + Firestore)                  │
└─────────────────────────────────────────────────────────┘
          │                      │
          ▼                      ▼
┌──────────────────┐    ┌──────────────────────────────┐
│  Firebase        │    │  HuggingFace Space (Docker)  │
│  ├─ 匿名 Auth    │    │  └─ FastAPI 後端              │
│  ├─ Google Auth  │    │     ├─ POST /chat             │
│  └─ Firestore    │    │     ├─ POST /narrate          │
│     ├─ users/    │    │     ├─ POST /tts              │
│     ├─ sessions/ │    │     ├─ POST /summarize        │
│     └─ counsel…/ │    │     ├─ POST /generate         │
└──────────────────┘    │     └─ GET  /health           │
                        │                              │
                        │  + OpenMythos (PyTorch)      │
                        │  + Gemini API (chat/TTS)     │
                        └──────────────────────────────┘
```

### 前端
| 技術 | 用途 |
|---|---|
| Three.js r128 + 自製 GLSL shader | 12,000 粒子即時變形 + 10 種動畫 |
| @mediapipe/hands | 手勢追蹤 |
| Web Speech API | 語音輸入(Chrome/Edge 最佳) |
| wordcloud2.js | 文字雲渲染 |
| Chart.js | 直方圖、折線圖 |
| Firebase JS SDK v11 | Auth + Firestore |
| 純 HTML + CSS + vanilla JS | 無 framework,易於部署 |

### 後端
| 技術 | 用途 |
|---|---|
| FastAPI + Uvicorn | REST API |
| Google GenAI SDK | Gemini 3.1 Flash TTS + Gemini Chat |
| OpenMythos | Recurrent-Depth Transformer(象徵性運算展示) |
| PyTorch | Mythos 模型推論 |

### 資料
| 技術 | 用途 |
|---|---|
| Firebase Firestore | 對話語料即時同步 |
| Security Rules | Owner-only read/write + Admin override |

---

## 🚀 本地啟動

### 1. 後端
```bash
# Clone OpenMythos (模型依賴)
git clone https://github.com/kyegomez/OpenMythos
pip install -e ./OpenMythos

# 安裝其他依賴
pip install -r requirements.txt

# 設定 Gemini API Key
cp .env.example .env
# 編輯 .env 填入你的 key: https://aistudio.google.com/app/apikey

# 啟動後端 (port 8000)
python mythos_server.py
```

### 2. 前端
```bash
python3 -m http.server 8080
# 打開 http://localhost:8080/
```

### 3. (必須) Firebase 設定
1. 到 [Firebase Console](https://console.firebase.google.com/) 建立專案
2. 啟用 **Authentication** → Anonymous + Google
3. 建立 **Firestore Database** (test mode)
4. 複製你的 `firebaseConfig` → 替換 `index.html` / `counseling.html` / `admin.html` 中的三處設定
5. 部署 `firestore.rules` 到 Firebase Console

---

## 📦 部署

| 服務 | 角色 | 成本 |
|---|---|---|
| **GitHub Pages** | 前端靜態託管 | 免費 |
| **HuggingFace Spaces (Docker)** | 後端 FastAPI + PyTorch | 免費 (CPU basic) |
| **Firebase** (Spark plan) | Auth + Firestore | 免費 |
| **Google AI Studio** | Gemini API Key | 免費 tier 或 Tier 1 付費 |

總部署成本:**$0 / 月**(試用規模內)

詳細步驟見 [`hf-space/README.md`](./hf-space/README.md)。

---

## 📄 論文研究應用

本系統設計時即考慮**教育科技研究**場景。Admin 後台可一鍵生成 APA-7 格式的完整論文骨架:

- **Methodology** 段落:自動描述資料蒐集方法、樣本數、分析工具
- **Results** 段落:5 張表格 + 對應解讀
  - Table 1 · 訊息長度描述統計
  - Table 2 · 年代參與度
  - Table 3 · KB 12 原則頻率
  - Table 4 · Bigram/Trigram Top 10
  - Table 5 · Bloom's 提問分類
- **Discussion** 段落:三項主要發現 + KB 密度指標討論
- **Limitations** 段落:5 項已內建

### 匯出格式
- `.md` — for LaTeX / Obsidian / HackMD
- `.html` — 可用 Word 直接開啟,Times New Roman 排版
- `.csv` — 丟 Excel / SPSS / R / pandas

---

## 📂 專案結構

```
taiwan-river-of-history/
├── index.html              # 主展覽 (粒子 + 手勢 + 語音)
├── counseling.html         # 諮商室 (唱片選擇 + KB 對話)
├── admin.html              # 管理後台 (語料分析 + APA 報告)
├── mythos_server.py        # FastAPI 後端
├── requirements.txt        # Python 依賴
├── firestore.rules         # Firestore 安全規則
├── .env.example            # 環境變數範本
└── hf-space/               # HuggingFace Space 部署檔
    ├── Dockerfile
    ├── README.md
    ├── requirements.txt
    └── mythos_server.py
```

---

## 🎯 商業應用方向

| 場景 | 切入點 |
|---|---|
| 🏛 博物館 / 國史館 / 文策院 | 互動展區、夜間投影 |
| 🎓 高中歷史科 / 108 課綱 | 輔助教材、探究與實作 |
| 🏢 企業 CSR / 政府部門 | 文化推廣、海外僑委會 |
| 🌏 觀光局 / 機場 / 捷運站 | 沉浸式藝術裝置 |
| 📊 教育科技研究 | KB discourse 實證研究平台 |

---

## 📜 授權

**MIT License** — 歡迎自由使用、改作、再發行。

---

## 🙏 致謝

- [OpenMythos](https://github.com/kyegomez/OpenMythos) by Kye Gomez — Recurrent-Depth Transformer
- [MediaPipe](https://developers.google.com/mediapipe) by Google — 手勢辨識
- [Gemini API](https://ai.google.dev/) — TTS + 對話引擎
- [Three.js](https://threejs.org/) — 3D 粒子渲染
- [Firebase](https://firebase.google.com/) — 即時資料庫與認證
- [Scardamalia & Bereiter (2014)](https://en.wikipedia.org/wiki/Knowledge_building) — Knowledge Building 12 Principles
- 所有曾在諮商室與島語對話過的訪客 — 你們的想法已成為這座島嶼的一部分。

---

<p align="center">
  <b>製作</b> · Ian3738 · 2026
</p>
