# 🔑 API Key 完整說明

## 你需要知道的一切

---

## 什麼是 API Key？

### 簡單比喻：
- **API Key** = 你的身份牌
- 就像你進辦公室需要員工卡
- Google Gemini 需要你的 Key 才知道是誰在使用

### 具體說：
1. Google 有個超強的 AI 模型（Gemini）
2. 你想在你的應用中使用它
3. 需要一個 Key 來證明你是誰
4. Google 通過 Key 追蹤誰在使用服務（免費額度用戶/付費用戶）

---

## 獲取 API Key 的完整步驟

### 第 1 步：打開瀏覽器

```
https://makersuite.google.com/app/apikey
```

### 第 2 步：登錄 Google 帳戶

- 如果已登入，自動進行
- 否則，點擊登錄

### 第 3 步：看到 API Keys 頁面

頁面上會顯示：
```
API keys
Create API key in new project [按鈕]
```

### 第 4 步：點擊按鈕

會彈出菜單：
- 選擇 "Create API key in new project"

### 第 5 步：複製你的 Key

會看到一個長字符串：
```
AIzaSyD-xhzqXvPUlVQfV-DlqL0p7u3qZpFVk-8
```

**這就是你的 API Key！** ✨

---

## API Key 的三種使用方式

### 方式 1️⃣：在 .env 文件中（推薦）

**創建 `.env` 文件：**

```bash
cat > .env << EOF
GOOGLE_API_KEY=AIzaSyD-xhzqXvPUlVQfV-DlqL0p7u3qZpFVk-8
EOF
```

**應用會自動讀取！**

### 方式 2️⃣：在應用界面輸入

1. 運行 `streamlit run app_gemini.py`
2. 在側邊欄看到 "Google API Key" 輸入框
3. 粘貼 API Key
4. 點擊 "Initialize Agent"

### 方式 3️⃣：部署到 Streamlit Cloud 時

1. 在 Streamlit Cloud 上設置 Secrets
2. 添加 `GOOGLE_API_KEY = "..."`
3. 應用自動使用

---

## 完整工作流程

```
┌─────────────────────────────────────────────┐
│ 1. 獲取 Google Gemini API Key               │
│    (https://makersuite.google.com/app/apikey)│
└─────────────┬───────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│ 2. 在應用中配置 API Key                     │
│    - .env 文件 或                           │
│    - 應用界面輸入 或                        │
│    - Streamlit Secrets                      │
└─────────────┬───────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│ 3. 運行應用                                 │
│    streamlit run app_gemini.py              │
└─────────────┬───────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│ 4. 應用通過 API Key 連接到 Google Gemini    │
│    並開始處理數據                           │
└─────────────┬───────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│ 5. 用戶可以提問並得到 AI 回答               │
└─────────────────────────────────────────────┘
```

---

## API Key 的安全性

### ✅ 安全做法：
- 使用 `.env` 文件
- 使用 Streamlit Secrets（部署時）
- 不要提交到 GitHub
- `.gitignore` 中已有 `.env`

### ❌ 不安全做法：
- 把 Key 寫在代碼裡
- 把 Key 分享給别人
- 上傳 Key 到 GitHub

### 如果 Key 洩露怎麼辦？
1. 立即刪除舊 Key
2. 在 Google AI Studio 生成新 Key
3. 更新 `.env` 或 Secrets
4. 沒有人能用舊 Key 了

---

## 免費額度

### 什麼是免費額度？
- Google 給免費用戶的使用量限制
- 超過限制需要付費

### Gemini 免費額度：
- **60 requests/分鐘**
- **完全免費**（無需信用卡）
- 適合個人使用和學習

### 舉例：
- 提一個問題 = 1 個請求
- 如果 60 秒內提超過 60 個問題 = 會被限制
- 但正常使用不會超限

### 超過限制？
1. 等一分鐘，計數器重置
2. 或者升級到付費方案

---

## 快速檢查清單

### ✅ 開始前：
- [ ] 有 Google 帳戶
- [ ] 能訪問 makersuite.google.com

### ✅ 獲取 API Key：
- [ ] 訪問 https://makersuite.google.com/app/apikey
- [ ] 登錄
- [ ] 點擊 "Create API Key"
- [ ] 複製 Key

### ✅ 配置應用：
- [ ] 創建 `.env` 文件 或 在應用界面輸入
- [ ] 添加 `GOOGLE_API_KEY=你的Key`

### ✅ 運行應用：
- [ ] `streamlit run app_gemini.py`
- [ ] 應用在 localhost:8501 打開
- [ ] 測試提問

### ✅ 部署（可選）：
- [ ] 推送到 GitHub
- [ ] Streamlit Cloud 配置 Secrets
- [ ] 點擊 Deploy

---

## 常見問題

| 問題 | 回答 |
|------|------|
| API Key 在哪？ | https://makersuite.google.com/app/apikey |
| 免費嗎？ | 是的，有免費額度 |
| 需要信用卡？ | 不需要 |
| 多少錢？ | 免費用戶 60 請求/分鐘 |
| Key 丟了怎麼辦？ | 生成新的 |
| Key 洩露了怎麼辦？ | 刪除舊的，生成新的 |
| 可以在代碼裡寫 Key 嗎？ | 不行！要用 .env 或 Secrets |
| 需要多少個 Key？ | 1 個就夠 |

---

## 📚 文件說明

| 文件 | 說明 |
|------|------|
| [QUICK_START_GEMINI.md](QUICK_START_GEMINI.md) | **快速開始（推薦先讀）** |
| [API_KEY_GUIDE.md](API_KEY_GUIDE.md) | 詳細的 API 說明 |
| [GEMINI_VERSION.md](GEMINI_VERSION.md) | Gemini 版本的完整文檔 |
| [app_gemini.py](app_gemini.py) | Gemini 版應用代碼 |
| [tools_gemini.py](tools_gemini.py) | Gemini Agent 邏輯 |
| [setup_gemini.sh](setup_gemini.sh) | 自動設置腳本 |

---

## 🚀 立即開始

**三步啟動：**

```bash
# 1. 獲取 API Key（網頁操作）
# 訪問：https://makersuite.google.com/app/apikey

# 2. 配置應用
bash setup_gemini.sh
# 或手動：echo "GOOGLE_API_KEY=..." > .env

# 3. 運行
streamlit run app_gemini.py
```

**完成！** ✨

---

## 💡 下一步

1. **現在：** 按照 [QUICK_START_GEMINI.md](QUICK_START_GEMINI.md) 開始
2. **測試：** 在本地運行應用
3. **優化：** 修改應用以適應你的需求
4. **部署：** 上傳到 Streamlit Cloud
5. **分享：** 給朋友們使用你的應用！

---

**一切都很簡單！現在就開始吧！** 🎉
