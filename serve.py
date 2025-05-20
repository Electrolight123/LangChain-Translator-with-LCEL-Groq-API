#%% Import Libraries

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import time
import threading
import webbrowser
import os
from dotenv import load_dotenv

load_dotenv()

#%% Load API Key

groq_api_key = os.getenv('GROQ_API_KEY')

#%% Load LLM

llm = ChatGroq(model="Gemma2-9b-It", api_key = groq_api_key,)
sys_temp = "You are a expericnced translator, please translate English input into {language}"
prompt = ChatPromptTemplate.from_messages(
    [('system', sys_temp), ('user', '{text}')])
parser = StrOutputParser()
chain = prompt|llm|parser

#%% Create App

app = FastAPI(title = 'Langchain Server', version = "beta 0", description = 'A Simple API for Langchain Runable Interface')
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)
add_routes(app = app, runnable = chain, path = '/chain')

#%% Open Browser

def open_browser():
    
    time.sleep(1.5)
    cwd = os.getcwd()
    html_path = os.path.join(cwd, 'index.html')
    webbrowser.open('file://' + html_path)

#%% Execute App

if __name__ == "__main__":
    import uvicorn
    threading.Thread(target=open_browser).start()
    uvicorn.run(app = app, host = "127.0.0.1", port = 8000)