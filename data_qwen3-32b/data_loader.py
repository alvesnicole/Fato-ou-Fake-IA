import os
import pandas as pd
import random

def _carregar_pasta(caminho, label, n_amostras):
    registros = []

    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Pasta não encontrada: {caminho}")

    arquivos = [f for f in os.listdir(caminho) if f.endswith(('.txt', '.csv'))]

    if not arquivos:
        raise ValueError(f"Nenhum arquivo .txt ou .csv em: {caminho}")

    random.shuffle(arquivos)

    for nome in arquivos:
        if len(registros) >= n_amostras:
            break
        caminho_arquivo = os.path.join(caminho, nome)
        try:
            if nome.endswith('.csv'):
                df_temp = pd.read_csv(caminho_arquivo)
                col_texto = None
                for candidata in ['text', 'texto', 'content', 'body', 'noticia']:
                    if candidata in df_temp.columns:
                        col_texto = candidata
                        break
                if col_texto is None:
                    col_texto = (df_temp.select_dtypes(include='object')
                                 .apply(lambda c: c.str.len().mean()).idxmax())
                for texto in df_temp[col_texto].dropna():
                    registros.append({'texto': str(texto).strip(), 'label_real': label})
                    if len(registros) >= n_amostras:
                        break
            else:
                with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
                    conteudo = f.read().strip()
                if conteudo:
                    registros.append({'texto': conteudo, 'label_real': label})
        except Exception as e:
            print(f"  [Aviso] Erro ao ler '{nome}': {e} — pulando.")

    return pd.DataFrame(registros)

def carregar_e_preparar_dados(caminho_fake, caminho_true, amostra_por_classe, seed=42):
    random.seed(seed)

    print("  Carregando notícias FALSAS...")
    df_fake = _carregar_pasta(caminho_fake, "FALSO", amostra_por_classe)
    print(f"    {len(df_fake)} notícias falsas carregadas.")

    print("  Carregando notícias VERDADEIRAS...")
    df_true = _carregar_pasta(caminho_true, "VERDADEIRO", amostra_por_classe)
    print(f"    {len(df_true)} notícias verdadeiras carregadas.")

    n = min(len(df_fake), len(df_true), amostra_por_classe)
    df_fake = df_fake.sample(n=n, random_state=seed).reset_index(drop=True)
    df_true = df_true.sample(n=n, random_state=seed).reset_index(drop=True)

    df = pd.concat([df_fake, df_true], ignore_index=True)
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    df['texto'] = df['texto'].str.strip()
    df = df[df['texto'].str.len() > 30].reset_index(drop=True)

    print(f"\n  Dataset final: {len(df)} notícias ({df['label_real'].value_counts().to_dict()})")
    return df