# 🌊 台灣歷史長河 · River of Formosa
## 完整製作文件 & 簡報素材

> 一座由粒子、聲音、對話與 AI 共構的**台灣史互動展覽**,搭載符合 Knowledge Building (KB) 12 原則的 AI 導覽員「島語」。從手勢探索到 KB 式深度諮商,從即時語音到語料研究後台,是一個完整的「**教育科技 × 互動藝術 × AI 對話**」作品。

**作者**:Ian3738
**完成日期**:2026 年 4 月
**技術規模**:約 8,000 行程式碼 / 15+ 項整合技術 / 3 個前端頁面 + 1 個後端服務
**線上連結**
- 🌐 **主展覽**:https://ian3738.github.io/taiwan-river-of-history/
- 💭 **諮商室**:https://ian3738.github.io/taiwan-river-of-history/counseling.html
- 📊 **語料分析後台**:https://ian3738.github.io/taiwan-river-of-history/admin.html
- 📦 **原始碼**:https://github.com/Ian3738/taiwan-river-of-history
- 🤗 **後端 Space**:https://huggingface.co/spaces/Ian3738/island-guide-server

---

## 📜 目錄

1. [專案緣起與核心概念](#1-專案緣起與核心概念)
2. [使用者可體驗的三個入口](#2-使用者可體驗的三個入口)
3. [開發歷程](#3-開發歷程)
4. [技術架構全覽](#4-技術架構全覽)
5. [14 個歷史節點設計](#5-14-個歷史節點設計)
6. [島語 AI 導覽員](#6-島語-ai-導覽員)
7. [知識翻新 KB 12 原則實作](#7-知識翻新-kb-12-原則實作)
8. [視覺設計系統](#8-視覺設計系統)
9. [互動模態:語音 / 手勢 / 觸控 / 鍵盤](#9-互動模態)
10. [資料蒐集與研究框架](#10-資料蒐集與研究框架)
11. [部署與基礎設施](#11-部署與基礎設施)
12. [商業應用方向](#12-商業應用方向)
13. [技術挑戰與解決方案](#13-技術挑戰與解決方案)
14. [未來路線圖](#14-未來路線圖)
15. [簡報素材:關鍵投影片](#15-簡報素材)

---

## 1. 專案緣起與核心概念

### 起點問題
傳統歷史教育三個痛點:
- **單向灌輸**:教科書陳述事實,學生被動記憶
- **單一視角**:漢人中心史觀為主,少見原住民、女性、勞工視角
- **時空脫節**:歷史像外在知識,與個人生命經驗斷裂

### 設計哲學
讓歷史變成**可觸摸、可聆聽、可對話的時空**。
讓 AI 不是**答題機器**,而是**共構思考的夥伴**(基於 KB 理論框架)。
讓每位訪客的**提問與觀察**都成為知識網絡的一部分。

### 核心概念:三層疊合

| 層次 | 內容 |
|---|---|
| 🎨 **感官層** | 12,000 顆粒子即時變形為歷史意象,手勢/語音/觸控多模態互動 |
| 💭 **對話層** | 島語 AI 以 KB 12 原則陪你深度探索,主動提問、引入多重視角 |
| 📊 **研究層** | 所有對話同步 Firestore,後台產出 APA-7 論文級分析報告 |

---

## 2. 使用者可體驗的三個入口

### 🎨 主展覽 `index.html`
12,000 粒子構成的台灣島嶼地圖作為開場,用戶可透過手勢、語音、觸控探索 14 個歷史節點。每個節點有專屬的粒子立體圖案(蒸汽火車、太陽花、玉山⋯)與即時動畫(海浪搖擺、地震衰減、花瓣綻放⋯)。

### 💭 島語諮商室 `counseling.html`
復古琥珀色調的「唱片式」介面,14 張歷史唱片橫向滑動選擇。懸停時黑膠從套中滑出旋轉,點選進入**諮商級深度對話**。3 種模式:年代專屬 / 自由對話 / 今日反思。

### 📊 語料分析後台 `admin.html`
管理員專用(Google OAuth + Firestore 安全規則)。7 個分頁:總覽、描述統計、文字雲、詞頻/N-gram、行為分析、KB 原則偵測、論文報告。可直接匯出 Markdown / HTML / CSV 格式的 APA-7 論文骨架。

---

## 3. 開發歷程

### Phase 1:技術探索
- 安裝 OpenMythos (Recurrent-Depth Transformer) 驗證可行性
- 建立 FastAPI 後端,暴露 `/generate` 端點
- 用 curl 確認模型推論正常 (1.5M 參數、譜半徑 ρ = 0.368)

### Phase 2:視覺原型
- Three.js + 粒子 shader 系統
- 12 種粒子形狀生成器(船、晶圓、向日葵、玉山、神經網絡⋯)
- 整合 MediaPipe Hands 做手勢控制

### Phase 3:AI 引擎整合
- 串接 Gemini 3.1 Flash TTS(島語的聲音)
- 串接 Gemini Flash 對話模型(KB system prompt)
- 設計 14 段歷史敘事(從使用者提供的腳本)

### Phase 4:研究基礎設施
- Firebase Auth(匿名 + Google)
- Firestore 儲存對話語料
- Firestore Security Rules 保護隱私
- 建立 admin.html 分析後台

### Phase 5:KB 對話深化
- 諮商室獨立頁面(counseling.html)
- 唱片式介面設計
- /summarize 端點產生 KB 結構化摘要
- KB 12 原則完整規則集偵測

### Phase 6:學術化與商業化
- APA-7 表格自動生成
- Markdown / HTML / CSV 論文匯出
- 描述統計、文字雲、N-gram、Bloom's 分類
- 島語 system prompt 明確範圍(聚焦台灣史、溫暖婉拒離題)

### Phase 7:優化與精修
- 預錄 14 段歷史敘事成靜態 wav(省 Gemini quota)
- 手勢誤觸防護(1 秒暖機期、_lastSpokenEraIdx 去重)
- 醒著時任何話都送 Gemini 自然回應(不再只認關鍵字)
- UI 各項細節調校(時間軸、對話框、手勢圖例字級)

---

## 4. 技術架構全覽

```
┌─────────────────────────────────────────────────────────────────┐
│  使用者瀏覽器 (Chrome / Edge / Safari / 手機瀏覽器)              │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  3 個前端頁面 (純 HTML + vanilla JS,無框架)              │  │
│  │  ├─ index.html        主展覽                              │  │
│  │  ├─ counseling.html   諮商室                              │  │
│  │  └─ admin.html        語料分析後台                         │  │
│  └──────────────────────────────────────────────────────────┘  │
│     │                                                           │
│     ├─ Three.js r128 + 自製 GLSL shader   (粒子視覺化)          │
│     ├─ @mediapipe/hands                    (手勢辨識)           │
│     ├─ Web Speech API                      (語音輸入)           │
│     ├─ Firebase JS SDK v11                 (Auth + Firestore)   │
│     ├─ wordcloud2.js                       (文字雲)             │
│     └─ Chart.js                            (統計圖表)           │
│                                                                 │
└───────────────────────┬─────────────────────────────────────────┘
                        │ HTTPS
          ┌─────────────┼──────────────┐
          ▼             ▼              ▼
┌───────────────┐ ┌───────────────┐ ┌─────────────────────┐
│   Firebase    │ │  HF Space     │ │  靜態檔案            │
│   (免費)      │ │  (Docker)     │ │  voices/*.wav       │
│               │ │               │ │  (GitHub Pages)     │
│ ├ 匿名 Auth   │ │ FastAPI 後端  │ │  20 個預錄語音檔     │
│ ├ Google Auth │ │  ├ /chat      │ │  總大小 ~15MB       │
│ ├ Firestore   │ │  ├ /tts       │ │                     │
│ │  ├ users/   │ │  ├ /summarize │ └─────────────────────┘
│ │  ├ sessions │ │  └ /health    │
│ │  └ counsel… │ │               │
│ └ Security    │ │ + PyTorch     │
│   Rules       │ │ + OpenMythos  │
│               │ │ + Gemini SDK  │
└───────────────┘ └───────┬───────┘
                          │
                          ▼
                  ┌────────────────┐
                  │  Gemini API    │
                  │  Flash + TTS   │
                  │  3.1 preview   │
                  └────────────────┘
```

### 技術棧詳細

| 層 | 技術 | 用途 |
|---|---|---|
| **3D 渲染** | Three.js r128 + 自製 GLSL | 12,000 粒子即時變形 + 10 種 shader 動畫 |
| **手勢辨識** | @mediapipe/hands | 食指撥動、捏合、握拳、指向 |
| **語音輸入** | Web Speech API (zh-TW) | 連續辨識 + interim results |
| **語音輸出** | Gemini 3.1 Flash TTS (Leda) + 預錄 WAV | 主要用預錄檔,fallback Gemini |
| **AI 對話** | Gemini Flash + KB system prompt | 聚焦台灣史的知識翻新對話 |
| **認證** | Firebase Auth (匿名 + Google) | 訪客匿名、管理員 Google |
| **資料庫** | Firestore | 即時對話同步、使用者 profile |
| **後端** | FastAPI + Uvicorn + Python | REST API |
| **模型** | OpenMythos (PyTorch, 1.5M params) | 象徵性運算展示(Mythos × Gemini 混合) |
| **部署 - 前端** | GitHub Pages (免費,HTTPS) | 靜態網站託管 |
| **部署 - 後端** | HuggingFace Spaces (Docker) | FastAPI + PyTorch 免費雲端 |
| **分析** | wordcloud2.js, Chart.js | 文字雲、直方圖、熱圖 |

---

## 5. 14 個歷史節點設計

| # | 年代 | 事件 | 粒子圖案 | 動畫 |
|---|---|---|---|---|
| 1 | ~4000 BCE | 南島語族的起源 | 🛶 獨木舟 + 海浪 | 海浪搖擺 |
| 2 | 1624 | 大航海的交會 | ⛵ 三桅大帆船 + 熱蘭遮城 | 海浪搖擺 |
| 3 | 1661 | 鄭氏東寧的孤光 | 🏯 書院牌樓 + 鄭成功劍 + 屯田格 | 靜態 |
| 4 | 1887 | 鐵路與電光之初 | 🚂 蒸汽火車 + 鐵軌 + 煙霧 | 火車前進 + 煙飄 |
| 5 | 1895 | 乙未割讓的斷柱 | 🏛 斷柱 + 撕裂的馬關條約 | 斷裂顫抖 |
| 6 | 1921 | 文化覺醒的年代 | 📖 開書 + 燈泡 + 擴音器 | 煙霧上升 |
| 7 | 1947 | 二二八的裂縫 | 🕯 碎裂石碑 + 三根紀念燭台 | 熄滅閃爍 |
| 8 | 1980 | 矽島的崛起 | 💾 半導體晶圓 + die 矩陣 | 晶圓自轉 |
| 9 | 1987 | 解嚴後的綻放 | 🕊 破曉飛鳥 + 朝陽 + 光芒 | 飛升 |
| 10 | 1996 | 首次總統直選 | 🗳 投票箱 + 台灣島輪廓 | 靜態 |
| 11 | 1999 | 九二一的搖晃 | 🌋 山脈震波 | **雷動衰減**(每 3 秒一次) |
| 12 | 2014 | 太陽花的春天 | 🌻 向日葵 | 花瓣綻放呼吸 |
| 13 | 2020 | 護國神山與口罩外交 | ⛰ 玉山 + 晶圓 + 口罩 | 靜態 |
| 14 | 2026 | AI 與共創時代 | 🧠 三層神經網絡 | 脈動同心波 |

### 設計原則
- **每個圖案都呼應敘事中的關鍵物件**(馬關條約、蠟燭、口罩...)
- **立體而非平面**:所有粒子形狀都有真實 3D 體積,旋轉時都可見
- **動畫對應情感**:地震用劇烈衰減震動、太陽花用溫柔呼吸、飛鳥用向上飛升
- **顏色有歷史指涉**:1947 暗紅(創傷)、1987 金黃(自由)、1980 琥珀(產業)

---

## 6. 島語 AI 導覽員

### 人格設定
- **名字**:島語 (Dǎo Yǔ,取「為島嶼發聲」之意)
- **角色**:以粒子凝聚而成的台灣史 AI 對話夥伴
- **性格**:溫暖、知性、略帶詩意,學者風格但結尾**必反問**
- **語言**:繁體中文(Gemini Leda 女聲)

### 能力範圍

✅ **可回答**:
- 台灣歷史事件、人物、時代背景(史前 → 當代)
- 台灣文化、社會、政治、經濟、教育、科技演變
- 族群:原住民、漢人、平埔、客家、外省、新住民
- 使用者個人/家族與台灣歷史的連結
- 多元視角、史學爭議、史料來源

❌ **溫暖婉拒**:
- 非台灣相關一般知識(如數學、程式)
- 時事政治評論、選舉預測
- 個人情感諮商 / 心理治療
- 違法、歧視、色情、暴力內容

**婉拒範例**:「這個問題有意思,但不在我專長的台灣歷史範圍內。如果你能把它連結到台灣的歷史或文化,我很樂意一起探索。」

### 五種提問應對策略
| 類型 | 應對方式 |
|---|---|
| 事實性 | 先給精準答案,再反問使用者的看法 |
| 情感性 | 承接情緒,引導到歷史共鳴 |
| 比較性 | 給多重視角,提醒歷史情境差異 |
| 推測性 | 坦承歷史不確定性,用「如果...會怎樣」思辨 |
| 家族故事 | 好奇提問,連到大歷史 |

### 語音指令能力
- 喚醒:「**島語**」(含多種誤聽變體:稻語、倒語、島嶼...)
- 導航:「太陽花」「1624」「護國神山」等年代關鍵字直接跳轉
- 操作:打開資訊卡、念給我聽、下一個、回到長河
- 停止:停止導覽、不要念了、暫停
- 對話:**醒著時任何話都會自動轉給 Gemini 自然回應**

---

## 7. 知識翻新 KB 12 原則實作

**理論基礎**:Scardamalia & Bereiter (2014), *Knowledge Building and Knowledge Creation: Theory, Pedagogy, and Technology*.

### 12 原則完整列表

| # | 中文完整名 | 英文原名 | 系統實作 |
|---|---|---|---|
| 1 | 從真實問題中瞭解真正的想法 | Real Ideas, Authentic Problems | system prompt 要求島語從訪客真正的好奇出發 |
| 2 | 不斷精進的想法 | Improvable Ideas | 絕不說「答錯」,改說「如果加上 X 會更完整」 |
| 3 | 想法的多樣性 | Idea Diversity | 主動引入原住民、女性、勞工、客家、外省多重視角 |
| 4 | 統整有助於想法昇華 | Rise Above | 對話累積後幫助統整出更高層次概念 |
| 5 | 知識為社群共創並負有共同責任 | Community Knowledge, Collective Responsibility | 適時提及「另一位訪客曾分享⋯」 |
| 6 | 知識創造為平等參與,成員的貢獻無法切割 | Democratizing Knowledge | 平等對話,不強調權威 |
| 7 | 知識翻新注重對話 | Knowledge Building Discourse | 每次回覆結尾必反問 |
| 8 | 認知能動性 / 知識的自主追求者 | Epistemic Agency | 讓訪客主導探究方向 |
| 9 | 內嵌的、即時的、變革性的評量 | Embedded, Concurrent, and Transformative Assessment | 給予肯定回饋「你的觀點很有深度」 |
| 10 | 互享共榮的知識翻新過程 | Symmetric Knowledge Advancement | 承認「這個角度我之前沒想過,謝謝你」 |
| 11 | 無所不在的知識翻新 | Pervasive Knowledge Building | 把歷史連到當下與訪客生活情境 |
| 12 | 建構性地運用權威資料 | Constructive Uses of Authoritative Sources | 引用《臺灣通史》《被出賣的台灣》等並說明「是其中一種說法」 |

### KB 原則偵測系統(admin.html)
用正則表達式規則集掃描每則島語回應,量化 12 原則出現頻率:

```javascript
{n:3, short:'想法多樣性', full:'想法的多樣性', en:'Idea Diversity',
 re:/換個角度|另一個角度|不同視角|從.{1,6}的立場|原住民|漢人|平埔|
     女性|男性|勞工|資本家|商人|農民|外省|本省|客家|左派|右派|多元|
     多重|另一面|反過來|相反的|另外一種|也有人認為|不同觀點/}
```

### KB 密度指標
自動計算「偵測次數 / 島語訊息數」,作為對話品質的**操作性定義**。
- ≥ 2.0:高密度,符合 KB 理論預期
- 1.0~2.0:中等,基本達標
- < 1.0:偏低,可能需要調校 system prompt

---

## 8. 視覺設計系統

### 配色 (三個頁面各自的調性)

**主展覽** — 深空科技感
- 主色:`#030308` 近黑背景
- 強調:`#00e5ff` 青 + `#e0a030` 琥珀
- 節點色:14 個年代各自的 Morandi 色系

**諮商室** — 復古溫暖感
- 主色:`#1a1612` → `#2b1e18` 暖褐漸層
- 強調:`#e0a030` 琥珀 + `#f0e0c0` 米白
- 唱片封套:從 DATA 的 node.color 延伸

**語料後台** — 研究專業感
- 主色:`#0a0a12` 深藍
- 強調:`#00e5ff` 青(資料)+ `#e0a030` 琥珀(標題)
- 紅色:`#ff8080` 僅用於警告

### 字型
- **中文標題**:Noto Serif TC(襯線,歷史感)
- **中文內文**:Noto Serif TC 1rem / 1.08rem / 1.1rem(提升可讀性)
- **英文標題**:Orbitron(科技感)
- **英文內文**:Noto Sans TC

### 可讀性原則
- 全站最小字 **14px** 起跳(避免小於 12px)
- 主要內文 **1-1.1rem** + 行高 **1.85-2.0**
- 對比度:白字最少 `rgba(255,255,255,.75)`
- 所有可點擊元素 ≥ 40x40px 觸控區

---

## 9. 互動模態

### 🎤 語音
- **辨識**:Web Speech API (zh-TW),continuous + interim
- **喚醒詞**:「島語」+ 20+ 個常見誤聽變體
- **智慧對話**:醒著時任何話都會送到 Gemini 取得 KB 風格回應
- **朗讀**:優先播放預錄 WAV(省 quota),fallback Gemini TTS
- **停止**:「停止導覽」「不要念了」「暫停」⋯

### 🤚 手勢 (MediaPipe Hands)
| 手勢 | 效果 |
|---|---|
| 食指撥動 (open palm + 水平速度) | 切換年代 |
| 食指指向滑動 | 旋轉粒子圖形 |
| 食指尖懸停資訊卡 1 秒 | 放大/縮小卡片 |
| 食指 + 大拇指捏合 | 場景縮放(單手) |
| 雙手拉開 | 雙手縮放 |
| 握拳 1 秒 | 回到長河 |

**防誤觸**:
- 手剛出現的 1 秒**暖機期** — 不觸發任何切換動作
- Swipe 冷卻 1500ms
- `_lastSpokenEraIdx` 去重,同年代不重念

### 📱 觸控
- 點選節點 → 切換
- 左右滑(>60px, <800ms) → 上/下一個年代
- 向下滑 → 回到長河
- 雙指捏合 → 場景縮放
- 點擊資訊卡 → 放大/縮小

### ⌨️ 鍵盤
- `← →` 切換年代
- `Esc` 回到長河
- `1-9` 直接跳該年代

---

## 10. 資料蒐集與研究框架

### Firestore 資料結構
```
users/{uid}/
  ├── nickname: "阿芸"
  ├── createdAt: <timestamp>
  ├── lastSeen: <timestamp>
  │
  ├── sessions/{sessionId}/          ← 主展覽的對話面板
  │     ├── startedAt, lastActive
  │     ├── lastEra
  │     └── messages/{auto-id}
  │           ├── role: user | guide
  │           ├── text
  │           ├── era
  │           └── timestamp
  │
  ├── counselingSessions/{sessionId}/   ← 諮商室深度對話
  │     ├── startedAt, lastActive, era, mode
  │     ├── summary                      ← Gemini 生成的摘要
  │     └── messages/{auto-id}
  │           └── (同上)
  │
  └── eraVisits/{auto-id}
        ├── sessionId, eraId, eraName
        └── timestamp
```

### 管理員後台分析功能

**描述統計**
- 中位數、平均數、標準差、P25/P75
- 訊息長度直方圖(8 個分組)
- 變異係數 CV 判讀離散度

**文字雲**(wordcloud2.js)
- 中文 N-gram 2-4 字分詞
- 70+ 停用詞過濾
- 可切換「全部 / 僅使用者 / 僅島語」

**詞頻分析**
- Top 30 高頻詞(雙欄比較使用者 vs 島語)
- Bigram Top 20
- Trigram Top 20

**行為分析**
- 7×24 活躍熱圖(週 × 時)
- 提問比例 + Bloom's Taxonomy 分類
  - Why 類 → Analyze 層級
  - How 類 → Apply 層級
  - 事實問題 → Remember 層級

**KB 原則偵測**
- 12 原則每條的出現次數
- KB 密度指標(條/則)
- 最強/最弱原則診斷

### 論文報告自動生成(APA-7 格式)
| 段落 | 自動內容 |
|---|---|
| Methodology | 資料蒐集期間 + 平台 + 匿名機制 + 四階段分析方法 |
| Table 1 | 訊息長度描述統計(全部/使用者/島語) |
| Table 2 | 14 年代參與度排名 |
| Table 3 | KB 12 原則頻率(含中英完整名稱) |
| Table 4 | Bigram × Trigram Top 10 |
| Table 5 | Bloom's 提問分類 |
| Discussion | 三項主要發現 + KB 密度討論 |
| Limitations | 5 項內建(樣本規模、關鍵字偵測、匿名限制等) |

### 匯出格式
- **Markdown** — LaTeX / Obsidian / HackMD
- **HTML** — 直接貼 Word / Google Docs(Times New Roman 排版)
- **CSV** — Excel / SPSS / R / pandas

---

## 11. 部署與基礎設施

### 架構選擇

| 服務 | 角色 | 費用 | 理由 |
|---|---|---|---|
| **GitHub Pages** | 前端 (HTML/JS/CSS/靜態音檔) | $0 | 免費、HTTPS、CDN 分發 |
| **HuggingFace Space** (Docker) | 後端 FastAPI + PyTorch | $0 | 免費 CPU 16GB,支援 PyTorch |
| **Firebase** (Spark plan) | Auth + Firestore | $0 | 個人使用量內免費 |
| **Gemini API** | 對話 + TTS | $0 | Tier 1 paid 信用卡,但免費額度充足 |

**總運行成本**:**$0 / 月**

### Firestore 安全規則重點
```javascript
function isOwner(userId) {
  return request.auth != null && request.auth.uid == userId;
}
function isAdmin() {
  return request.auth != null && request.auth.uid == 'ADMIN_UID';
}

match /users/{userId} {
  allow read: if isOwner(userId) || isAdmin();
  allow list: if isAdmin();
  allow create, update: if isOwner(userId) && validProfile(request.resource.data);
  allow delete: if isAdmin();
  ...
}
```

- 普通訪客:只能讀寫自己的 `users/{uid}`
- 管理員:固定 UID 可讀所有使用者、可刪除
- 訊息寫入後不可修改(`allow update: if false`)— 保證歷史完整性

### 部署流程
```
1. git push master → GitHub Pages 自動部署 (1 分鐘)
2. cp mythos_server.py hf-space/ && push HF → Docker 自動 rebuild (5-10 分鐘)
3. Firebase Console 手動貼 firestore.rules → Publish
4. 若 TTS quota 耗盡 → python scripts/generate_voices.py 重新批次生成
```

---

## 12. 商業應用方向

| 場景 | 切入點 | 規模 |
|---|---|---|
| 🏛 **博物館 / 國史館 / 文策院** | 互動展區、夜間投影、兒童探索區 | NT$ 80-300 萬 / 案 |
| 🎓 **高中歷史科 / 108 課綱** | 輔助教材、探究與實作 | NT$ 30-100 萬 授權 |
| 🏢 **企業 CSR / 政府** | 文化推廣、僑委會海外宣傳 | NT$ 100-200 萬 客製 |
| 🌏 **觀光局 / 機場 / 捷運站** | 沉浸式藝術裝置 | NT$ 200 萬+ / 案 |
| 📊 **教育科技研究** | KB discourse 實證研究平台 | 學術合作 / 論文發表 |

### 作為作品集的優勢
- **跨領域整合**:AI × 前端 × 教育理論 × 視覺藝術 × 資料分析
- **完整的產品思維**:從 UI 到後端到研究工具,不只是 demo
- **可立即體驗**:線上連結點開就玩,不用 setup
- **學術深度**:內建 KB 理論、APA 論文報告、可投 EdTech 期刊
- **商業可行**:$0 成本運行,證明小團隊也能做

---

## 13. 技術挑戰與解決方案

### 挑戰 1:Gemini TTS quota 每日 100 次上限
**解決**:
- 預錄 14 段歷史敘事 + 6 句常用對白為靜態 `.wav`
- 前端優先播放預錄檔,只有動態內容才呼叫 API
- `scripts/generate_voices.py` 支援增量生成(已存在的跳過)

### 挑戰 2:手勢辨識在鏡頭閃斷/光線變化時誤觸發
**解決**:
- 手剛出現的 1 秒**暖機期**
- Swipe 冷卻延長到 1500ms
- `_lastSpokenEraIdx` 防止同年代重念
- 捏合不再清 aiCache 觸發重新朗讀

### 挑戰 3:GLSL shader 編譯失敗靜默當機
**原因**:一個缺失的分號導致整個 shader 編譯失敗,粒子完全不顯示
**解決**:嚴格檢查所有 if block 閉合、避免 `normalize(0)` NaN

### 挑戰 4:HTML 原生 `disabled` 無法用 CSS 覆蓋
**症狀**:`body.named #go{opacity:1}` 看起來能點,實際 browser 阻擋 click event
**解決**:JS `removeAttribute('disabled')` 實際移除屬性

### 挑戰 5:語音重複朗讀 / Gemini 被呼叫多次
**原因**:`setTimeout` 閉包抓到舊的 aiCache 物件;renderAi 被 UI 事件頻繁觸發
**解決**:
- `r.spoken` 旗標確保每段只念一次
- `aiCache[idx]===r` 檢查防止陳舊 timeout 觸發
- 朗讀邏輯從 `renderAi` 集中到 `selectNode` 單一入口

### 挑戰 6:Firebase 匿名 UID 跨裝置不同
**影響**:研究分析時同一使用者可能被當成不同人
**目前處理**:localStorage 保持瀏覽器內 UID 穩定
**未來方向**:Google Sign-In 整合(讓有需要的使用者選擇綁定)

### 挑戰 7:Firestore Rules 要允許管理員看所有使用者但禁止一般訪客
**解決**:固定管理員 UID 在 rules 中
```
function isAdmin() {
  return request.auth != null && request.auth.uid == 'hardcoded_admin_uid';
}
allow list: if isAdmin();  // 只有管理員能列出所有 users
```

---

## 14. 未來路線圖

### 短期 (1-3 個月)
- [ ] 接入 ElevenLabs TTS(音質更自然,替代 Gemini preview 模型的 quota 限制)
- [ ] 添加更多歷史節點(牡丹社事件、霧社事件、美麗島事件)
- [ ] 中文分詞採用 jieba(替代現在的 N-gram 近似)
- [ ] KB 原則偵測改用 BERT-based classifier(提高準確度)
- [ ] 多語言(英文、日文)讓國際觀眾使用

### 中期 (3-12 個月)
- [ ] 開放 API 讓老師自製互動展覽
- [ ] AR 版本(手機打開鏡頭看現實世界,粒子疊加)
- [ ] 多使用者同時對話(同一年代的共同討論)
- [ ] 情境式情緒分析(sentiment analysis 標記每則訊息)
- [ ] A/B test 工具,比較不同對話策略的 KB 觸發率

### 長期
- [ ] 發表教育科技論文(CSCL / Computers & Education)
- [ ] 與博物館合作實體裝置展覽
- [ ] 開源變成 KB 對話平台模板,適用其他學科(地理、生物、文學)

---

## 15. 簡報素材

### 🎯 30 秒電梯簡報(Elevator Pitch)

> **台灣歷史長河**是一座由 12,000 顆粒子凝聚而成的互動展覽,搭載名為「島語」的 AI 導覽員。訪客可以用手勢、語音、觸控瀏覽 14 個歷史節點,每一個都變形為該時代的立體圖案——蒸汽火車、太陽花、玉山、神經網絡。島語不只朗讀歷史,更以**知識翻新 12 原則**引導訪客從多重視角反思。所有對話同步到雲端,後台可一鍵生成 **APA-7 格式的論文分析報告**。這是一個結合 AI、互動藝術、教育理論的完整作品,**運行成本 $0**,**線上可直接體驗**。

### 📊 三頁簡報大綱

**Slide 1:問題 × 願景**
- 傳統歷史教育的三個痛點(單向、單視角、時空脫節)
- 設計哲學:讓歷史變成可觸摸、可對話的時空
- 三層疊合架構(感官 / 對話 / 研究)

**Slide 2:產品展示**
- 14 個歷史節點 × 粒子立體圖案
- 主展覽 / 諮商室 / 後台 三個入口
- Live demo QR code

**Slide 3:技術 × 研究**
- 技術棧全圖(Three.js / MediaPipe / Gemini / Firebase)
- KB 12 原則實作表
- APA-7 論文報告樣張

### 🎬 Demo 流程建議(3 分鐘)
1. **[0:00]** 打開主頁 → 看到台灣粒子島嶼
2. **[0:15]** 取名:「叫我阿芸」→ 島語確認
3. **[0:30]** 說「**島語,帶我去太陽花**」→ 粒子變形為向日葵,朗讀歷史
4. **[1:00]** 說「**為什麼太陽花學運重要?**」→ 島語用 KB 風格回應
5. **[1:30]** 右上 ❓ → 展示手勢/語音/觸控三種互動
6. **[2:00]** 切到 💭 諮商室 → 展示唱片式介面
7. **[2:15]** 切到 📊 後台 → 展示文字雲 + KB 密度 + APA 論文匯出
8. **[2:45]** 結語:$0 成本、開源、可複製到任何文化場景

### 🗣 常見問答準備

**Q:這和一般的歷史網站差在哪?**
A:多了 AI 對話、多模態互動、研究框架。不只「看」歷史,而是「**和歷史對話、被歷史提問**」。

**Q:為什麼選 KB 原則而非標準 QA?**
A:KB 原則是國際認可的合作學習理論(Scardamalia & Bereiter)。強調**想法精進**和**多重視角**,這正是台灣史教育最需要的 — 跳出單一史觀。

**Q:語料分析有實際研究價值嗎?**
A:所有對話都有 KB 原則標記、可匯出 CSV,可直接做卡方檢定、時序分析、主題建模。是可複製的 AI-mediated KB discourse 研究基礎設施。

**Q:商業模式?**
A:不走 SaaS,走**內容授權 / 展覽委託 / 教育整合**。博物館、高中歷史科、政府文化部門是主要目標。

**Q:為什麼取名「島語」?**
A:「為島嶼發聲的人」。台灣曾經很少人為它發聲,這個 AI 想補上那個位置。

---

## 📎 附錄

### 專案檔案結構
```
taiwan-river-of-history/
├── index.html              # 主展覽 (約 3,500 行)
├── counseling.html         # 諮商室 (約 650 行)
├── admin.html              # 管理後台 (約 1,500 行)
├── mythos_server.py        # FastAPI 後端
├── requirements.txt        # Python 依賴
├── firestore.rules         # Firestore 安全規則
├── .env.example            # 環境變數範本
├── .gitignore
├── README.md               # 專案總覽
├── PROJECT_DOCUMENTATION.md  # 本文件
├── scripts/
│   └── generate_voices.py   # 批次生成語音工具
├── voices/                  # 預錄語音檔 (15MB)
│   ├── era_bce4000.wav → era_2026.wav (14 個)
│   └── line_*.wav (6 個常用對白)
└── hf-space/                # HF Space 部署檔
    ├── Dockerfile
    ├── README.md
    ├── requirements.txt
    └── mythos_server.py
```

### 主要依賴版本
```
# Python
fastapi >= 0.110
uvicorn >= 0.30
pydantic >= 2.0
torch >= 2.1
google-generativeai >= 0.8
google-genai >= 0.3
python-dotenv >= 1.0
firebase-admin (非必要,目前用 client SDK)

# 前端 (CDN)
three@r128
@mediapipe/hands@0.4.1675469240
firebase-app@11.0.2
firebase-auth@11.0.2
firebase-firestore@11.0.2
wordcloud@1.2.2
chart.js@4.4.0
```

### 致謝
- [OpenMythos](https://github.com/kyegomez/OpenMythos) — Recurrent-Depth Transformer
- [MediaPipe](https://developers.google.com/mediapipe) by Google — 手勢辨識
- [Gemini API](https://ai.google.dev/) — TTS + 對話引擎
- [Three.js](https://threejs.org/) — 3D 粒子渲染
- [Firebase](https://firebase.google.com/) — 即時資料庫與認證
- Scardamalia & Bereiter — Knowledge Building 12 Principles

---

**製作**:Ian3738 · 2026
**授權**:MIT License
**原始碼**:https://github.com/Ian3738/taiwan-river-of-history
