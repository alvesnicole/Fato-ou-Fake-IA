import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")
GROQ_KEY = os.getenv("GROQ_API_KEY")

MODELOS = ["groq/llama-3.3-70b-versatile"]
AMOSTRA_POR_CLASSE = 100         # 200 notícias no total (100 fake + 100 true)
CAMINHO_FAKE = 'data/fake'
CAMINHO_TRUE = 'data/true'