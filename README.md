# 🌐 LangChain Translator with LCEL + Groq API

This is a simple LLM-based translation web app built using **LangChain**, **LCEL**, **Groq API**, and **FastAPI**, with a modern HTML frontend. The app allows users to translate English text into any target language using open-source LLMs like **Gemma**, **LLaMA3**, or **Mistral**.

---

## 📁 Project Structure

```
LangChain-Translator-with-LCEL-Groq-API/
│
├── simplellmLCL.ipynb # Notebook showing LangChain workflow
├── index.html # Frontend HTML UI for translation
├── serve.py # FastAPI backend serving LangChain chain
├── .env # Environment variables (API keys etc.)
├── requirements.txt # Required Python packages
├── README.md # Project documentation (you are here!)
```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the repository

```bash
git clone https://github.com/yourusername/simplellmLCL.git
cd simplellmLCL
```

### 🐍 2. Create and activate a virtual environment (recommended)
Using `venv`:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📦 3. Install required dependencies

```bash
pip install -r requirements.txt
```

### 🔑 4. Set up your .env file
Create a `.env` file in the root directory with the following content (replace with your actual API keys):

```
GROQ_API_KEY="your_groq_api_key"
```

## 🚀 Running the Application
### ▶️ Start the backend server

```bash
python serve.py
```

This will:
* Launch a **FastAPI** server at `http://127.0.0.1:8000`
* Serve the LangChain chain at endpoint `/chain/invoke`
* Open the `index.html` file in your browser automatically

# 🌐 Use the Web App

The web UI allows users to:

*Enter a target language
*Enter text in English
*Click Translate to get output using Groq-powered open-source models

