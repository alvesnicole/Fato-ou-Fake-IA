import pandas as pd
import os
import time
from config import MODELOS, CAMINHO_FAKE, CAMINHO_TRUE, AMOSTRA_POR_CLASSE
from data_loader import carregar_e_preparar_dados
from engine import classificar_texto
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def executar_experimento():
    print("\n--- Iniciando Experimento de ML ---")

    if not os.path.exists("results"):
        os.makedirs("results")

    df = carregar_e_preparar_dados(CAMINHO_FAKE, CAMINHO_TRUE, AMOSTRA_POR_CLASSE)
    print(f"Dataset pronto: {len(df)} notícias.")

    for mod in MODELOS:
        print(f"\n>>> Avaliando: {mod}")
        predicoes = []
        tempos = []

        total = len(df)
        # FIX: usar enumerate para garantir contador correto independente do índice do DataFrame
        for idx, (_, row) in enumerate(df.iterrows()):
            print(f"  Progresso: {idx+1}/{total}", end="\r")
            pred, lat = classificar_texto(row['texto'], mod)
            predicoes.append(pred)
            tempos.append(lat)
            time.sleep(2.5)

        df[f'pred_{mod}'] = predicoes
        df[f'lat_{mod}'] = tempos

        print(f"\n\n=== Relatório para {mod} ===")
        df_valid = df[df[f'pred_{mod}'] != "ERRO"]
        erros = len(df) - len(df_valid)
        if erros > 0:
            print(f"  Notícias com erro (excluídas das métricas): {erros}")

        if not df_valid.empty:
            print(classification_report(
                df_valid['label_real'],
                df_valid[f'pred_{mod}'],
                target_names=["FALSO", "VERDADEIRO"]
            ))

            cm = confusion_matrix(
                df_valid['label_real'],
                df_valid[f'pred_{mod}'],
                labels=["FALSO", "VERDADEIRO"]
            )
            plt.figure(figsize=(6, 5))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                        xticklabels=["FALSO", "VERDADEIRO"],
                        yticklabels=["FALSO", "VERDADEIRO"])
            nome_limpo = mod.replace("/", "_")
            plt.title(f"Matriz de Confusão — {nome_limpo}")
            plt.ylabel("Real")
            plt.xlabel("Predito")
            plt.tight_layout()
            plt.savefig(f"results/confusion_{nome_limpo}.png", dpi=150)
            plt.close()
            print(f"  Matriz salva em results/confusion_{nome_limpo}.png")

            lat_media = df_valid[f'lat_{mod}'].mean()
            print(f"  Latência média por requisição: {lat_media:.2f}s")

    df.to_csv("results/experimento_final.csv", index=False)
    print("\nProcesso finalizado. Arquivos salvos em /results")

if __name__ == "__main__":
    executar_experimento()
