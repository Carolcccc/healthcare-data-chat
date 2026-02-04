# 🌟 Gemini Version - Setup Guide

## 概述 (Overview)

這是 Healthcare AI Agent 的 **Google Gemini** 版本。與 Ollama 版本不同，這個版本：

- ✅ 使用 Google Gemini API（雲端運行）
- ✅ **可以部署**到 Streamlit Cloud
- ✅ 不需要本地運行 LLM
- ⚠️ 需要 Google API Key（免費額度可用）

## 🔑 獲取 API Key

1. 訪問：https://makersuite.google.com/app/apikey
2. 使用 Google 帳戶登錄
3. 點擊 "Create API Key"
4. 複製你的 API key

**免費額度：**
- 每分鐘 60 次請求
- 足夠個人使用和測試

## 🚀 本地運行

### 方法 1: 使用 .env 文件

1. 創建 `.env` 文件：
```bash
echo "GOOGLE_API_KEY=你的API密鑰" > .env
```

2. 運行 Streamlit：
```bash
streamlit run app_gemini.py
```

3. Agent 會自動讀取 API key

### 方法 2: 在 UI 中輸入

1. 運行 Streamlit：
```bash
streamlit run app_gemini.py
```

2. 在側邊欄輸入你的 API key
3. 點擊 "Initialize Agent"

### CLI 版本

```bash
# 設置環境變數
export GOOGLE_API_KEY=你的API密鑰

# 運行
python main_gemini.py
```

## ☁️ 部署到 Streamlit Cloud

### 步驟 1: 推送到 GitHub

```bash
git add app_gemini.py tools_gemini.py main_gemini.py
git commit -m "Add Gemini version"
git push origin main
```

### 步驟 2: 在 Streamlit Cloud 部署

1. 訪問 https://share.streamlit.io
2. 連接你的 GitHub repository
3. 選擇 `app_gemini.py` 作為主文件
4. 在 "Advanced settings" → "Secrets" 中添加：

```toml
GOOGLE_API_KEY = "你的API密鑰"
```

5. 點擊 Deploy！

### 步驟 3: 修改代碼以使用 Secrets（如果部署）

如果要從 Streamlit Secrets 讀取 API key，可以修改 `app_gemini.py`：

```python
# 在文件開頭添加
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    os.environ["GOOGLE_API_KEY"] = api_key
except:
    pass  # 如果沒有 secrets，用戶可以手動輸入
```

## 📊 文件說明

```
healthcare_ai_agent/
├── app.py              # Ollama 版本（本地）
├── app_gemini.py       # Gemini 版本（可部署）✨ 新增
├── main.py             # Ollama CLI
├── main_gemini.py      # Gemini CLI ✨ 新增
├── tools.py            # Ollama agent
├── tools_gemini.py     # Gemini agent ✨ 新增
├── prompts.py          # 共用系統提示詞
└── requirements.txt    # 已更新包含 Gemini
```

## 💰 成本說明

**免費額度：**
- Gemini Pro API 有免費層級
- 每分鐘 60 次請求
- 適合個人使用和演示

**付費使用：**
- 如果超過免費額度
- 查看定價：https://ai.google.dev/pricing

**建議：**
- 用於教育演示：免費額度足夠
- 生產環境：需要監控使用量

## ⚖️ 兩個版本的比較

| 特性 | Ollama 版本 | Gemini 版本 |
|------|------------|------------|
| 成本 | 完全免費 | 免費額度 + 可能付費 |
| 部署 | ❌ 不能部署 | ✅ 可以部署 |
| 速度 | 快（本地M4） | 取決於網絡 |
| 隱私 | 完全本地 | 雲端處理 |
| 設置 | 需要安裝 Ollama | 只需 API key |
| 適用場景 | 本地開發/演示 | 在線部署/分享 |

## 🎯 使用建議

**使用 Ollama 版本（app.py）當：**
- ✅ 在自己電腦上使用
- ✅ 需要完全隱私
- ✅ 不想付 API 費用
- ✅ 有 Apple Silicon Mac

**使用 Gemini 版本（app_gemini.py）當：**
- ✅ 想部署給別人使用
- ✅ 需要在線訪問
- ✅ 在作品集中展示
- ✅ 沒有 Ollama 環境

## 📝 注意事項

1. **API Key 安全：**
   - 不要提交 API key 到 GitHub
   - 使用 `.env` 或 Streamlit Secrets
   - 定期輪換 API keys

2. **免責聲明：**
   - 兩個版本都有相同的法律保護
   - 僅用於教育目的
   - 不用於醫療診斷

3. **監控使用：**
   - 檢查 API 使用量
   - 設置預算警報
   - 防止濫用

## 🚀 快速開始

**本地測試：**
```bash
# 安裝依賴
pip install langchain-google-genai

# 設置 API key
export GOOGLE_API_KEY=你的密鑰

# 運行
streamlit run app_gemini.py
```

**部署到雲端：**
1. 推送代碼到 GitHub
2. 在 Streamlit Cloud 選擇 `app_gemini.py`
3. 添加 API key 到 Secrets
4. 部署！

---

**現在你有兩個版本可以選擇使用！** 🎉
