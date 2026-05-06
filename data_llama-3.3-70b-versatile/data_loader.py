import os
import pandas as pd

def carregar_e_preparar_dados(path_fake, path_true, n_amostra):
    def ler_pasta(pasta, rotulo):
        dados = []
        for arq in os.listdir(pasta):
            if arq.endswith(".txt"):
                with open(os.path.join(pasta, arq), 'r', encoding='utf-8') as f:
                    dados.append({"texto": f.read(), "label_real": rotulo})
        return pd.DataFrame(dados)

    df_fake = ler_pasta(path_fake, 'FALSO')
    df_true = ler_pasta(path_true, 'VERDADEIRO')

    df_f = df_fake.sample(n_amostra, random_state=42)
    df_t = df_true.sample(n_amostra, random_state=42)

    return pd.concat([df_f, df_t]).sample(frac=1, random_state=42).reset_index(drop=True)