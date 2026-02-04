#!/bin/bash

# Healthcare AI Agent - Gemini 版本快速設置腳本

echo "🏥 Healthcare AI Agent - Gemini 版本設置"
echo "=========================================="
echo ""

# 檢查是否已有 .env 文件
if [ -f .env ]; then
    echo "⚠️  .env 文件已存在"
    read -p "要覆蓋嗎？(y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "✅ 保持現有的 .env 文件"
        exit 0
    fi
fi

echo ""
echo "📌 步驟 1：獲取 Google Gemini API Key"
echo "訪問：https://makersuite.google.com/app/apikey"
echo ""

read -p "粘貼你的 API Key：" api_key

if [ -z "$api_key" ]; then
    echo "❌ API Key 不能為空"
    exit 1
fi

# 創建 .env 文件
cat > .env << EOF
# Google Gemini API Configuration
# Get your free API key at: https://makersuite.google.com/app/apikey
GOOGLE_API_KEY=$api_key
EOF

echo ""
echo "✅ .env 文件已創建！"
echo ""
echo "📌 步驟 2：安裝依賴"

# 檢查虛擬環境
if [ ! -d "venv" ]; then
    echo "創建虛擬環境..."
    python3 -m venv venv
fi

# 激活虛擬環境
source venv/bin/activate

# 安裝依賴
pip install -q langchain-google-genai

echo "✅ 依賴已安裝！"
echo ""
echo "🚀 步驟 3：啟動應用"
echo ""
echo "運行以下命令啟動應用："
echo ""
echo "  streamlit run app_gemini.py"
echo ""
echo "應用會在 http://localhost:8501 打開"
echo ""
echo "✨ 設置完成！"
