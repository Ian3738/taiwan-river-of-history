---
title: 島語 Mythos Server
emoji: 🌊
colorFrom: blue
colorTo: yellow
sdk: docker
app_port: 7860
pinned: false
license: mit
short_description: Backend for 台灣歷史長河 — Mythos × Gemini × Knowledge Building
---

# 島語 Mythos Server

台灣歷史長河 ([taiwan-river-of-history](https://github.com/Ian3738/taiwan-river-of-history)) 的後端 API:

- `POST /chat` — 與島語 KB 對話 (Gemini Chat Session)
- `POST /narrate` — Mythos 潛在空間運算 + Gemini 歷史敘事
- `POST /tts` — Gemini 2.5 Native TTS
- `POST /generate` — 純 Mythos 推論
- `GET /health` — 模型存活與譜半徑

## 設定

需要在 Space Settings → Repository secrets 新增:

- `GEMINI_API_KEY` — 你的 Gemini API Key

## 本地測試

```bash
docker build -t island-guide-server .
docker run -p 7860:7860 -e GEMINI_API_KEY=你的key island-guide-server
```
