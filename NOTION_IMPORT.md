# 🌊 River of Formosa · 台灣歷史長河

> 一座由粒子、聲音、對話與 AI 共構的台灣史互動展覽。
> 用手勢、語音、觸控走過六千年的島嶼記憶,搭載以知識翻新 (KB) 12 原則為核心的 AI 導覽員「島語」。

---

## 🔗 快速連結

| | |
|---|---|
| 🌐 **主展覽(可立即體驗)** | https://ian3738.github.io/taiwan-river-of-history/ |
| 💭 **島語諮商室** | https://ian3738.github.io/taiwan-river-of-history/counseling.html |
| 📊 **語料分析後台** | https://ian3738.github.io/taiwan-river-of-history/admin.html |
| 📦 **GitHub 原始碼** | https://github.com/Ian3738/taiwan-river-of-history |
| 🤗 **後端 API Space** | https://huggingface.co/spaces/Ian3738/island-guide-server |

---

## ✨ 一句話

**讓歷史變成可觸摸、可聆聽、可對話的時空。**

---

## 🎯 專案緣起

傳統歷史教育的三個痛點:

- **單向灌輸** — 教科書陳述事實,學生被動記憶
- **單一視角** — 漢人中心史觀為主,少見原住民、女性、勞工視角
- **時空脫節** — 歷史像外在知識,與個人生命經驗斷裂

因此設計這個作品,用三層疊合的架構來回應:

| 層次 | 內容 |
|---|---|
| 🎨 **感官層** | 12,000 顆粒子即時變形為歷史意象,手勢 / 語音 / 觸控多模態互動 |
| 💭 **對話層** | 島語 AI 以 KB 12 原則陪你深度探索,主動提問、引入多重視角 |
| 📊 **研究層** | 所有對話同步 Firestore,後台產出 APA-7 論文級分析報告 |

---

## 🎨 三個體驗入口

### 1️⃣ 主展覽
12,000 粒子構成的台灣島嶼地圖作為開場,用戶可透過手勢、語音、觸控探索 14 個歷史節點。每個節點有專屬的粒子立體圖案(蒸汽火車、太陽花、玉山⋯)與即時動畫(海浪搖擺、地震衰減、花瓣綻放⋯)。

### 2️⃣ 島語諮商室
復古琥珀色調的「唱片式」介面,14 張歷史唱片橫向滑動選擇。懸停時黑膠從套中滑出旋轉,點選進入**諮商級深度對話**。3 種模式:年代專屬 / 自由對話 / 今日反思。

### 3️⃣ 語料分析後台
管理員專用,Google OAuth + Firestore 安全規則保護。**7 個分頁**:總覽、描述統計、文字雲、詞頻/N-gram、行為分析、KB 原則偵測、論文報告。可直接匯出 Markdown / HTML / CSV 格式的 APA-7 論文骨架。

---

## 📍 14 個歷史節點

| 年代 | 事件 | 粒子圖案 | 動畫 |
|---|---|---|---|
| ~4000 BCE | 南島語族的起源 | 🛶 獨木舟 + 海浪 | 海浪搖擺 |
| 1624 | 大航海的交會 | ⛵ 三桅大帆船 + 熱蘭遮城 | 海浪搖擺 |
| 1661 | 鄭氏東寧的孤光 | 🏯 書院牌樓 + 鄭成功劍 | 靜態 |
| 1887 | 鐵路與電光之初 | 🚂 蒸汽火車 + 鐵軌 | 火車前進 + 煙飄 |
| 1895 | 乙未割讓的斷柱 | 🏛 斷柱 + 撕裂的馬關條約 | 斷裂顫抖 |
| 1921 | 文化覺醒的年代 | 📖 開書 + 燈泡 + 擴音器 | 煙霧上升 |
| 1947 | 二二八的裂縫 | 🕯 碎裂石碑 + 三根紀念燭台 | 熄滅閃爍 |
| 1980 | 矽島的崛起 | 💾 半導體晶圓 + die 矩陣 | 晶圓自轉 |
| 1987 | 解嚴後的綻放 | 🕊 破曉飛鳥 + 朝陽 | 飛升 |
| 1996 | 首次總統直選 | 🗳 投票箱 + 台灣島輪廓 | 靜態 |
| 1999 | 九二一的搖晃 | 🌋 山脈震波 | 雷動衰減 |
| 2014 | 太陽花的春天 | 🌻 向日葵 | 花瓣綻放呼吸 |
| 2020 | 護國神山與口罩外交 | ⛰ 玉山 + 晶圓 + 口罩 | 靜態 |
| 2026 | AI 與共創時代 | 🧠 三層神經網絡 | 脈動同心波 |

---

## 🧠 島語:以 KB 12 原則為核心的 AI 導覽員

**名字**:島語 (Dǎo Yǔ)
**意涵**:為島嶼發聲的人
**聲音**:Gemini 3.1 Flash TTS · Leda 女聲
**性格**:溫暖、知性、略帶詩意;學者風格,但結尾必反問

### 能力範圍

**✅ 可回答**
- 台灣歷史事件、人物、時代背景(史前 → 當代)
- 台灣文化、社會、政治、經濟、教育、科技演變
- 族群:原住民、漢人、平埔、客家、外省、新住民
- 使用者個人 / 家族與台灣歷史的連結
- 多元視角、史學爭議、史料來源

**❌ 溫暖婉拒**
- 非台灣相關一般知識(數學、程式、美國歷史等)
- 時事政治評論、選舉預測
- 個人情感諮商 / 心理治療
- 違法、歧視、色情、暴力內容

### 五種提問應對策略

| 類型 | 應對方式 |
|---|---|
| 事實性 | 先給精準答案,再反問使用者的看法 |
| 情感性 | 承接情緒,引導到歷史共鳴 |
| 比較性 | 給多重視角,提醒歷史情境差異 |
| 推測性 | 坦承歷史不確定性,用「如果⋯會怎樣」思辨 |
| 家族故事 | 好奇提問,連到大歷史 |

---

## 📚 知識翻新 KB 12 原則

理論基礎:**Scardamalia & Bereiter (2014)**, *Knowledge Building and Knowledge Creation*.

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

## 🎮 互動模態

### 🎤 語音
- **喚醒詞**:「島語」(支援 20+ 種常見誤聽變體)
- **直接跳轉**:「帶我去太陽花」「1624」「護國神山」
- **深度對話**:醒著時任何話都能自然回應
- **停止**:「停止導覽」「不要念了」「暫停」

### 🤚 手勢 (MediaPipe Hands)
| 手勢 | 效果 |
|---|---|
| 食指撥動 | 切換年代 |
| 食指指向滑動 | 旋轉粒子圖形 |
| 指尖懸停資訊卡 1 秒 | 放大 / 縮小 |
| 單手捏合 | 場景縮放 |
| 握拳 1 秒 | 回到長河 |

### 📱 觸控
- 點選節點 · 左右滑切換 · 雙指捏合 · 點擊卡片放大

### ⌨️ 鍵盤
- `← →` 切換 · `Esc` 回到長河 · `1-9` 直接跳該年代

---

## 🏗 技術架構

### 技術棧

| 層 | 技術 |
|---|---|
| 3D 視覺 | Three.js r128 + 自製 GLSL shader |
| 手勢辨識 | @mediapipe/hands |
| 語音輸入 | Web Speech API (zh-TW) |
| 語音輸出 | Gemini 3.1 Flash TTS + 預錄 WAV |
| AI 對話 | Gemini Flash + KB system prompt |
| 認證 | Firebase Auth (匿名 + Google) |
| 資料庫 | Firestore |
| 後端 | FastAPI + Uvicorn + Python |
| 模型 | OpenMythos (PyTorch, 1.5M params) |
| 前端部署 | GitHub Pages |
| 後端部署 | HuggingFace Spaces (Docker) |
| 分析 | wordcloud2.js + Chart.js |

### 基礎設施

| 服務 | 用途 | 成本 |
|---|---|---|
| GitHub Pages | 前端靜態託管 | $0 |
| HuggingFace Space | 後端 FastAPI | $0 |
| Firebase | Auth + Firestore | $0 |
| Gemini API | TTS + 對話 | $0 (免費額度) |

**總運行成本:$0 / 月**

---

## 📊 語料分析後台

### 可做的分析

- **描述統計**:中位數、標準差、P25/P75、訊息長度直方圖
- **文字雲**:150 個高頻詞,可切換使用者 vs 島語
- **詞頻 / N-gram**:Top 30 詞、Bigram、Trigram
- **活躍熱圖**:7 × 24 小時訊息密度分布
- **提問分類**:Bloom's Taxonomy(Why / How / Fact)
- **KB 原則偵測**:12 原則各自出現頻率,KB 密度指標

### 論文級報告(APA-7 格式)

自動生成:

- **Methodology** 段落:資料蒐集方法、樣本、分析工具
- **Results** 5 張表格:描述統計、年代參與度、KB 原則、N-gram、Bloom's 提問
- **Discussion** 段落:三項主要發現 + KB 密度討論
- **Limitations** 段落:5 項內建研究限制

### 匯出格式

- 📄 Markdown — LaTeX / Obsidian / HackMD
- 📄 HTML — 貼 Word / Google Docs(Times New Roman 排版)
- 📄 CSV — Excel / SPSS / R / pandas

---

## 💼 商業應用方向

| 場景 | 切入點 | 預期規模 |
|---|---|---|
| 🏛 博物館 / 國史館 / 文策院 | 互動展區、夜間投影 | NT$ 80-300 萬 / 案 |
| 🎓 高中歷史科 / 108 課綱 | 探究與實作、輔助教材 | NT$ 30-100 萬 授權 |
| 🏢 企業 CSR / 政府 | 文化推廣、僑委會海外宣傳 | NT$ 100-200 萬 客製 |
| 🌏 觀光局 / 機場 / 捷運站 | 沉浸式藝術裝置 | NT$ 200 萬+ / 案 |
| 📊 教育科技研究 | KB discourse 實證研究平台 | 學術合作 / 論文發表 |

---

## 🛠 開發歷程(7 個階段)

1. **技術探索** — 驗證 OpenMythos + FastAPI 可行
2. **視覺原型** — Three.js 粒子系統 + MediaPipe 手勢
3. **AI 引擎整合** — Gemini TTS + Chat + KB system prompt
4. **研究基礎設施** — Firebase Auth + Firestore + 安全規則
5. **KB 對話深化** — 諮商室獨立頁面 + /summarize 端點
6. **學術化與商業化** — APA-7 表格 + 論文匯出 + 聚焦台灣史
7. **優化與精修** — 預錄語音檔 + 手勢防誤觸 + 智慧對話 fallback

---

## 🧩 技術挑戰與解決

| 挑戰 | 解法 |
|---|---|
| Gemini TTS 每日 100 次 quota | 預錄 14 段敘事為靜態 wav |
| 手勢誤觸觸發重複朗讀 | 1 秒暖機期 + `_lastSpokenEraIdx` 去重 |
| GLSL shader 分號缺失靜默當機 | 嚴格檢查閉合 + 避免 `normalize(0)` |
| HTML `disabled` 無法用 CSS 覆蓋 | JS `removeAttribute()` 實際移除 |
| setTimeout 閉包抓舊 aiCache | `spoken` 旗標 + 物件引用檢查 |
| 匿名 UID 跨裝置不同 | localStorage 保持 + Google Sign-In 選項 |
| Firestore Rules 管理員權限 | `isAdmin()` 函式 + 固定 UID |

---

## 🔮 未來路線圖

### 短期 (1-3 個月)

- [ ] 接入 ElevenLabs TTS(更自然音質)
- [ ] 添加更多歷史節點(牡丹社事件、霧社事件、美麗島事件)
- [ ] 中文分詞改用 jieba
- [ ] KB 原則偵測改用 BERT classifier

### 中期 (3-12 個月)

- [ ] 多語言(英文、日文)
- [ ] 開放 API 讓老師自製互動展覽
- [ ] AR 版本(手機鏡頭疊加粒子)
- [ ] 多使用者同時對話(同年代的共同討論)

### 長期

- [ ] 發表教育科技論文(CSCL / Computers & Education)
- [ ] 博物館實體裝置合作
- [ ] 開源為 KB 對話平台模板

---

## 🎤 30 秒 Elevator Pitch

> 台灣歷史長河是一座由 12,000 顆粒子凝聚而成的互動展覽,搭載名為「島語」的 AI 導覽員。訪客可以用手勢、語音、觸控瀏覽 14 個歷史節點,每一個都變形為該時代的立體圖案——蒸汽火車、太陽花、玉山、神經網絡。
>
> 島語不只朗讀歷史,更以**知識翻新 12 原則**引導訪客從多重視角反思。所有對話同步到雲端,後台可一鍵生成 **APA-7 格式的論文分析報告**。
>
> 這是一個結合 AI、互動藝術、教育理論的完整作品,**運行成本 $0**,**線上可直接體驗**。

---

## 🗣 常見問答

### Q:這和一般的歷史網站差在哪?
A:多了 AI 對話、多模態互動、研究框架。不只「看」歷史,而是「**和歷史對話、被歷史提問**」。

### Q:為什麼選 KB 原則而非標準 QA?
A:KB 原則是國際認可的合作學習理論(Scardamalia & Bereiter)。強調**想法精進**和**多重視角**,這正是台灣史教育最需要的 — 跳出單一史觀。

### Q:語料分析有實際研究價值嗎?
A:所有對話都有 KB 原則標記、可匯出 CSV,可直接做卡方檢定、時序分析、主題建模。是可複製的 AI-mediated KB discourse 研究基礎設施。

### Q:商業模式?
A:不走 SaaS,走**內容授權 / 展覽委託 / 教育整合**。博物館、高中歷史科、政府文化部門是主要目標。

### Q:為什麼取名「島語」?
A:「為島嶼發聲的人」。台灣曾經很少人為它發聲,這個 AI 想補上那個位置。

---

## 📎 致謝

- **OpenMythos** by Kye Gomez — Recurrent-Depth Transformer
- **MediaPipe** by Google — 手勢辨識
- **Gemini API** — TTS + 對話引擎
- **Three.js** — 3D 粒子渲染
- **Firebase** — 即時資料庫與認證
- **Scardamalia & Bereiter** — Knowledge Building 12 Principles

---

**製作** · Ian3738 · 2026
**授權** · MIT License

---

## 📬 聯絡

如果你是博物館、學校、文化單位,對這個作品的應用有興趣,歡迎聯絡討論合作。
