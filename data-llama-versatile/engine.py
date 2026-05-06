import time
import litellm
from config import GROQ_KEY

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
        "Responda exclusivamente com uma das palavras: VERDADEIRO ou FALSO."
    )

    MAX_RETRIES = 5
    for tentativa in range(MAX_RETRIES):
        try:
            start = time.time()

            response = litellm.completion(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=5,
            )
            resultado = response.choices[0].message.content.strip().upper()
            duracao = time.time() - start
            final = "VERDADEIRO" if "VERDADEIRO" in resultado else "FALSO"
            return final, duracao

        except litellm.RateLimitError as e:
            msg = str(e)
            # Extrai o tempo de espera sugerido pelo Groq se disponível
            espera = 60 * (tentativa + 1)  # fallback: 60s, 120s, 180s...
            if "Please try again in" in msg:
                try:
                    trecho = msg.split("Please try again in")[1].split(".")[0].strip()
                    # converte "2m57s" ou "44s" para segundos
                    if "m" in trecho:
                        partes = trecho.replace("s", "").split("m")
                        espera = int(partes[0]) * 60 + int(partes[1] or 0)
                    else:
                        espera = int(trecho.replace("s", ""))
                    espera += 5  # margem de segurança
                except Exception:
                    pass
            print(f"\n[Rate limit] Tentativa {tentativa+1}/{MAX_RETRIES}. "
                  f"Aguardando {espera}s...")
            time.sleep(espera)

        except Exception as e:
            print(f"\n[Erro] {modelo}: {e}")
            return "ERRO", 0

    print(f"\n[Erro] Limite de tentativas atingido para esta notícia.")
    return "ERRO", 0