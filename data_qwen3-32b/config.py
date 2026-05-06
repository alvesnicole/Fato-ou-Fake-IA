import os
from dotenv import load_dotenv

load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY")
MODELOS = ["qwen/qwen3-32b"]

AMOSTRA_POR_CLASSE = 100
CAMINHO_FAKE = 'data/fake'
CAMINHO_TRUE = 'data/true'