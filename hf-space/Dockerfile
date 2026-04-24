# HuggingFace Spaces — Mythos × Gemini 後端 (FastAPI + PyTorch)
FROM python:3.11-slim

WORKDIR /app

# 系統依賴
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Python 依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 安裝 OpenMythos (從 GitHub clone)
RUN git clone --depth 1 https://github.com/kyegomez/OpenMythos.git /tmp/OpenMythos \
    && pip install --no-cache-dir /tmp/OpenMythos

# 複製應用程式
COPY mythos_server.py .

# HF Spaces 預設 port
EXPOSE 7860

# 啟動 FastAPI (注意:HF Spaces 必須監聽 0.0.0.0 + port 7860)
CMD ["uvicorn", "mythos_server:app", "--host", "0.0.0.0", "--port", "7860"]
