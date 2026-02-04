# 🏥 Healthcare AI Agent

A locally-powered healthcare data analysis agent using **Llama 3.2** on Apple M4 Mac via Ollama. Built with Streamlit, LangChain, and Pandas for interactive medical dataset exploration.

## ✨ Features

- 🤖 **Local AI Processing** - Runs Llama 3.2 entirely on your M4 Mac (no API keys needed)
- 💬 **Interactive Chat Interface** - Natural language queries for healthcare data
- 📊 **Real-time Analysis** - Instant insights from medical datasets
- 🎨 **Medical-Themed UI** - Professional healthcare styling
- 🔒 **Privacy-First** - All data processing happens locally

## 🚀 Quick Start

**⚠️ IMPORTANT: Please read [TERMS.md](TERMS.md) before using this application.**

### Prerequisites

- Apple M4 Mac (or compatible Apple Silicon)
- Python 3.9+
- Ollama installed

### 1. Install Ollama

Download from [ollama.ai](https://ollama.ai/download) or:

```bash
brew install ollama
```

Start Ollama and pull Llama 3.2:

```bash
ollama serve
ollama pull llama3.2
```

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/healthcare_ai_agent.git
cd healthcare_ai_agent
```

### 3. Download the Dataset

Download the healthcare dataset from Kaggle:
- **Dataset**: [Healthcare Dataset](https://www.kaggle.com/) (replace with actual link)
- Place the downloaded CSV file as `healthcare_dataset.csv` in the project root

### 4. Set Up Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Prepare the Data

```bash
python prepare_data.py
```

This creates `healthcare_dataset_cleaned.csv` with:
- No missing values
- Standardized date formats
- Removed duplicates

### 6. Run the Application

**Option A: Web Interface (Streamlit)**

```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser.

**Option B: Command Line**

```bash
python main.py
```

## 📁 Project Structure

```
healthcare_ai_agent/
├── app.py                          # Streamlit web interface
├── main.py                         # CLI version
├── tools.py                        # Agent creation logic
├── prompts.py                      # System prompts
├── config.py                       # Configuration (not used with Ollama)
├── prepare_data.py                 # Data cleaning script
├── requirements.txt                # Python dependencies
├── healthcare_dataset.csv          # Raw data (download separately)
└── healthcare_dataset_cleaned.csv  # Cleaned data (generated)
```

## 💡 Example Questions

Once the agent is initialized, try asking:

- "What is the average age of patients?"
- "How many patients have Diabetes?"
- "What is the most common medical condition?"
- "Show me the distribution of blood types"
- "What is the average billing amount?"
- "How many patients were admitted urgently?"

## 🛠️ Technology Stack

- **LLM**: Llama 3.2 (via Ollama)
- **Framework**: LangChain
- **UI**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn

## 📊 Dataset Information

The dataset contains healthcare records with the following columns:
- Name, Age, Gender, Blood Type
- Medical Condition, Date of Admission, Discharge Date
- Doctor, Hospital, Insurance Provider
- Billing Amount, Room Number, Admission Type
- Medication, Test Results

**Note**: The dataset is open-source from Kaggle. You must download it separately as it's too large for GitHub.

## 🔒 Privacy & Security

- ✅ All processing happens locally on your machine
- ✅ No data is sent to external APIs
- ✅ No API keys or sensitive credentials required
- ✅ Dataset should not contain real patient information (synthetic data)

## 🌟 Gemini (Cloud) Version

This repo also includes an optional Gemini version that **does not use my API key** and is safe to share.
You (or anyone using the repo) must bring your own Google Gemini API key.

- Streamlit app: app_gemini.py
- CLI: main_gemini.py
- Agent: tools_gemini.py

Setup guides:
- [QUICK_START_GEMINI.md](QUICK_START_GEMINI.md)
- [GEMINI_VERSION.md](GEMINI_VERSION.md)
- [API_KEY_GUIDE.md](API_KEY_GUIDE.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Important Notes

1. **Dataset Not Included**: Download the dataset separately from Kaggle
2. **Ollama Required**: Must have Ollama running with Llama 3.2 model
3. **M4 Mac Optimized**: Best performance on Apple Silicon (M4)
4. 🌐 Deployment

**Thinking of deploying this app?** 

📖 **Read [DEPLOYMENT.md](DEPLOYMENT.md) first** for critical legal and technical considerations.

**Short version:**
- ✅ Okay for educational demos and portfolios
- ❌ NOT for clinical/medical use
- ⚠️ Keep all disclaimers visible
- 📝 Consult legal counsel if unsure

## 📚 Documentation

- [README.md](README.md) - This file (setup guide)
- [TERMS.md](TERMS.md) - Terms of service and disclaimers
- [DEPLOYMENT.md](DEPLOYMENT.md) - Deployment guide and warnings
- [DATASET.md](DATASET.md) - Dataset download instructions
- [LICENSE](LICENSE) - MIT License with medical disclaimers

## 💬 Connect

Welcome to connect and share feedback or ideas!

- GitHub: https://github.com/Carolcccc
- Email: hsingchen28@gmail.com

## **Synthetic Data**: Use only synthetic/anonymized healthcare data

## ⚠️ Disclaimers

### Medical Disclaimer
**THIS SOFTWARE IS FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY.**

This application is NOT intended to provide medical advice, diagnosis, or treatment. The information generated should NOT be used as a substitute for professional medical advice.

- ❌ Do NOT use for medical diagnosis
- ❌ Do NOT use for treatment decisions  
- ❌ Do NOT replace professional medical consultation
- ✅ Use ONLY for learning and data exploration

**ALWAYS consult qualified healthcare professionals for medical decisions.**

### AI Disclaimer
This application uses AI/Large Language Models which may produce inaccurate or misleading information. All outputs should be verified independently.

### Data Privacy
Only use synthetic or anonymized data. Never upload real patient information or personally identifiable healthcare data.

## 📝 License

This project is open source and available under the MIT License with important disclaimers included. See [LICENSE](LICENSE) file for full terms and conditions.

**USE AT YOUR OWN RISK. NO WARRANTY PROVIDED.**

## 🙏 Acknowledgments

- Dataset from Kaggle (please cite the original source)
- Powered by Ollama and Llama 3.2
- Built with LangChain and Streamlit

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ for healthcare data analysis on Apple M4**
