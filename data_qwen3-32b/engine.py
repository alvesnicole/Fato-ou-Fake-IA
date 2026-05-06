import re
import time
from groq import Groq
from config import GROQ_KEY

client = Groq(api_key=GROQ_KEY)

MAX_ESPERA = 120  # cap absoluto de 2 minutos

def _parse_espera(msg, fallback):
    try:
        if "Please try again in" not in msg:
            return fallback
        trecho = msg.split("Please try again in")[1].split(".")[0].strip()

        match_ms = re.search(r"(\d+(?:\.\d+)?)ms", trecho)
        if match_ms:
            return max(2, int(float(match_ms.group(1)) / 1000) + 1)

        match_minsec = re.search(r"(\d+)m(\d+(?:\.\d+)?)s", trecho)
        if match_minsec:
            return int(int(match_minsec.group(1)) * 60 + float(match_minsec.group(2))) + 5

        match_s = re.search(r"(\d+(?:\.\d+)?)s", trecho)
        if match_s:
            return int(float(match_s.group(1))) + 5

        return fallback
    except Exception:
        return fallback

def classificar_texto(texto, modelo):
    prompt = (
        "Você é um sistema especializado em detecção de desinformação. "
        "Sua tarefa é classificar a notícia abaixo como VERDADEIRO (notícia legítima) "
        "ou FALSO (notícia fabricada, enganosa ou sem embasamento factual).\n\n"
        "Critérios de classificação:\n"
        "- VERDADEIRO: conteúdo jornalístico com fatos verificáveis, fontes identificáveis "
        "e linguagem neutra.\n"
        "- FALSO: conteúdo sensacionalista, sem fontes, com afirmações inverificáveis, "
        "linguagem tendenciosa ou deliberadamente enganoso.\n\n"
        f"Notícia:\n{texto[:800]}\n\n"
        "Responda exclusivamente com uma das palavras: VERDADEIRO ou FALSO. "
        "Não explique. Não raciocine. Responda apenas a palavra."
    )

    MAX_RETRIES = 5
    for tentativa in range(MAX_RETRIES):
        try:
            start = time.time()
            response = client.chat.completions.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=512,
            )
            conteudo = response.choices[0].message.content.strip()
            duracao = time.time() - start

            # Remove bloco <think>...</think> que o Qwen3 injeta
            if "</think>" in conteudo:
                conteudo = conteudo.split("</think>")[-1].strip()

            resultado = conteudo.upper()

            if "VERDADEIRO" in resultado:
                return "VERDADEIRO", duracao
            elif "FALSO" in resultado:
                return "FALSO", duracao
            else:
                print(f"\n[Aviso] Resposta inesperada: '{resultado[:80]}' — marcando como ERRO.")
                return "ERRO", duracao

        except Exception as e:
            msg = str(e)
            if "429" in msg or "rate" in msg.lower():
                fallback = 30 * (tentativa + 1)
                espera = min(_parse_espera(msg, fallback), MAX_ESPERA)
                print(f"\n[Rate limit] Tentativa {tentativa+1}/{MAX_RETRIES}. Aguardando {espera}s...")
                time.sleep(espera)
            else:
                print(f"\n[Erro inesperado]: {e}")
                return "ERRO", 0

    print(f"\n[Erro] Limite de tentativas atingido para este texto.")
    return "ERRO", 0
