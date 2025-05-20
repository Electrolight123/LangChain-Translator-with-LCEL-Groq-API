# 🌐 LangChain Translator with LCEL + Groq API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-orange)

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

## 🌐 Use the Web App

The web UI allows users to:

*Enter a target language
*Enter text in English
*Click **Translate** to get output using **Groq-powered open-source models**

## 📓 Jupyter Notebook Usage

The `simplellmLCL.ipynb` notebook walks through:

* Setting up LangChain with **OpenAI** or **Groq**
* Using **PromptTemplates** and `StrOutputParser`
* Building a translation chain using **LangChain Expression Language (LCEL)**
* Testing and invoking models directly in Python

## ✅ Requirements
These are included in `requirements.txt`:
```
ipykernel
fastapi
sse_starlette
langchain-groq
python-dotenv
openai
langserve
langchain_openai
uvicorn
```

## 🧠 Tech Stack

* **LangChain**: LLM chaining and prompt templating
* **Groq**: Fast inference on open-source models (Gemma, LLaMA3, Mistral)
* **FastAPI**: Backend API
* **LangServe**: Serve LangChain chains as APIs
* **HTML + JS**: Frontend user interface

## 📌 Example API Call

To test the API manually using `curl`:

```
curl -X POST http://127.0.0.1:8000/chain/invoke \
-H "Content-Type: application/json" \
-d '{"input": {"language": "French", "text": "Hello, how are you?"}}'
```

## 🛡️ Notes

* Make sure your `.env` file is correctly loaded and all keys are valid.
* Ensure you have internet access to contact **Groq/OpenAI** endpoints.
* For deployment, consider using `ngrok`, `Docker`, or platforms like **Render**, **Railway**, or **Fly.io**.

## 📄 License
This project is licensed under the **MIT License**. You're free to fork, modify, and build upon it.

## 🤝 Contributing
PRs and suggestions are welcome! If you find bugs or have enhancement ideas, feel free to open an issue.


