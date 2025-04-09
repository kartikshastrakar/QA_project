# 📚 LLM-Powered PDF/CSV QA System

A Retrieval-Augmented Generation (RAG) system powered by a Local LLM using Ollama that lets users upload PDF and CSV files and ask natural language questions based strictly on the content. Out-of-scope questions are gracefully declined.

> Built with ⚙️ LangChain, 🧠 LangGraph, 🧲 FAISS, and 🎨 Streamlit

---

## 🚀 Features

- ✅ PDF and CSV ingestion and parsing  
- ✅ Text chunking + semantic embeddings  
- ✅ Vector search using FAISS  
- ✅ Ollama-powered local LLM inference  
- ✅ Agentic RAG flow with LangGraph  
- ✅ Interactive Streamlit chat UI  
- ✅ Detects and declines out-of-scope queries  
- ✅ Multi-file (PDF + CSV) reasoning  

---

## 🛠️ Installation

### 📋 Prerequisites  
- Python 3.8+  
- Ollama installed and running (`ollama run mistral`)

### 🔧 Setup Steps  
1. Clone the repository  
   `git clone https://github.com/kartikshastrakar/QA_project.git && cd QA_project`  
2. Create virtual environment  
   `python -m venv venv`  
3. Activate environment  
   Windows: `venv\Scripts\activate`  
   macOS/Linux: `source venv/bin/activate`  
4. Install dependencies  
   `pip install -r requirements.txt`

---

## 🚀 Running the App

### 🧪 Option 1: Terminal (CLI)  
Run: `python scripts/main.py`  
- Place files in the `data/` folder  
- You'll be prompted to ask a question

### 🌐 Option 2: Streamlit Web Interface  
Run: `streamlit run app.py`  
- Upload PDF and/or CSV files  
- Ask questions in the chatbox  
- View file-based responses  

**Note:** Make sure Ollama is running: `ollama run mistral`

---

## 📂 Project Structure

QA_project/  
├── app.py – Streamlit web UI  
├── requirements.txt – Python dependencies  
├── README.md – Project documentation  
├── data/ – Input PDFs and CSVs  
│   ├── sales_data.csv  
│   └── sample_report.pdf  
├── vector_index/ – FAISS index storage  
├── scripts/  
│   ├── main.py – CLI pipeline  
│   └── workflow.png – Workflow image  
├── src/  
│   ├── document_processing/  
│   │   ├── loaders.py – PDF & CSV loaders  
│   │   └── splitters.py – Text chunking logic  
│   ├── embeddings/  
│   │   └── faiss_store.py – Embedding + FAISS  
│   └── llm/  
│       └── ollama_integration.py – Local LLM  
├── tests/ – Unit tests  
│   ├── test_loaders.py  
│   ├── test_splitters.py  
│   ├── test_faiss_store.py  
│   └── test_ollama.py  
└── evaluation.py – Optional: Model evaluation

---

## 📊 Workflow Diagram  
![Workflow Diagram](scripts/workflow.png)

---

## 📁 Sample Files & Example Questions

### ✅ Sample CSV  
Date,Product,Region,Units Sold,Revenue  
2025-01-05,UltraWidget 3000,North America,150,45000  
2025-01-06,MegaWidget 2000,Europe,80,16000  
2025-01-07,UltraWidget 3000,Asia,200,60000  
2025-01-08,MegaWidget 2000,North America,120,24000

### 📄 Sample PDF  
Includes product overview, strategic goals for 2025, and regional plans.

### 💡 Valid Example Questions  
- What is the total revenue for UltraWidget 3000?  
- How many units of MegaWidget 2000 were sold in Europe?  
- What is the strategy for expanding in Asia?  
- What was the revenue on 2025-01-05?

### ❌ Out-of-Scope Questions  
- Who is the CEO of Tesla?  
- What is the capital of Germany?

---

## ✅ Running Tests  
Use: `pytest tests/`

---

## 🎥 Demo  
[▶️ Demo Video](https://github.com/kartikshastrakar/QA_project/blob/main/20250408143245.mp4)

---

## 🧠 Acknowledgements  
- LangChain  
- LangGraph  
- FAISS by Meta  
- Ollama

---

## 📜 License  
MIT License

---

## 🤝 Need Help?  
Open an issue or reach out if you need help setting it up or customizing it for your use case!
