# Fake News Detection Experiment

Este repositório contém um ambiente de testes para classificação de notícias (**Verdadeiro** ou **Falso**) utilizando Modelos de Linguagem de Grande Escala (LLMs) via API do **Groq**.

O experimento foi estruturado para avaliar a precisão e a latência de diferentes modelos ao lidar com informações do cenário brasileiro.

## Tema/Problema Abordado

O projeto aborda o problema da detecção automática de fake news utilizando Modelos de Linguagem de Grande Escala (LLMs). O foco principal é analisar a capacidade desses modelos em identificar notícias falsas e verdadeiras em português, considerando desempenho de classificação e tempo de resposta.

## Objetivo do Trabalho

O objetivo deste trabalho é avaliar a eficiência de diferentes LLMs na tarefa de classificação de notícias do dataset Fake.br-Corpus, medindo:

- Precisão das classificações
- Recall e F1-Score
- Latência das respostas
- Robustez em cenários reais de desinformação

## O Dataset

Para este experimento, selecionamos **400 notícias** extraídas do dataset *Fake.br-Corpus*.

Embora tenhamos focado nestas 400 amostras específicas para nossos testes, o código é totalmente compatível com qualquer recorte ou notícia adicional do dataset original.

### Controle de Fluxo

O script está configurado para processar **200 notícias por execução**. Essa estratégia foi adotada para respeitar rigorosamente os limites de tokens (*Rate Limits*) e garantir a estabilidade durante as chamadas aos modelos:

- `llama-3.3-70b-versatile`
- `qwen3-32b`

---

## Técnicas/Modelos Utilizados

### Técnicas

- Classificação textual supervisionada
- Prompt Engineering
- Avaliação automática de desempenho
- Balanceamento de classes
- Geração de matrizes de confusão

### Modelos

- `llama-3.3-70b-versatile`
- `qwen3-32b`

---

## Bibliotecas e Ferramentas Empregadas

### Bibliotecas Python

- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `python-dotenv`
- `groq`

### Ferramentas

- API Groq
- Fake.br-Corpus
- Python 3
- Ambiente virtual (`venv`)

---

## Estrutura do Projeto

```plaintext
├── data_llama-3.3-70b-versatile/
│   ├── data/                       # Notícias verdadeiras e falsas do experimento
│   ├── results/                    # CSVs e matrizes geradas pelo modelo
│   ├── .env                        # Chave de autenticação da API Groq
│   ├── config.py                   # Modelos, caminhos e tamanho das amostras
│   ├── data_loader.py              # Carregamento, balanceamento e preparação textual
│   ├── engine.py                   # Classificação automática e controle de rate limits
│   └── main.py                     # Execução, métricas e geração dos resultados
│
├── data_qwen3-32b/
│   ├── data/                       # Notícias verdadeiras e falsas do experimento
│   ├── results/                    # CSVs e matrizes geradas pelo modelo
│   ├── .env                        # Chave de autenticação da API Groq
│   ├── config.py                   # Modelos, caminhos e tamanho das amostras
│   ├── data_loader.py              # Carregamento, balanceamento e preparação textual
│   ├── engine.py                   # Classificação automática e controle de rate limits
│   └── main.py                     # Execução, métricas e geração dos resultados
│
├── README.md
├── requirements.txt
└── comparacao_modelos.ipynb
```

## Como Executar o Projeto

### 1. Instalação das Dependências

Ative seu ambiente virtual (`venv`) e instale as dependências:

```bash
pip install -r requirements.txt
```

### 2. Configuração da API

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
```

### 3. Organização dos Dados

As notícias devem estar organizadas na pasta `data/`, separadas entre:

```plaintext
data/
├── fake/
└── true/
```

### 4. Execução

Execute o experimento com:

```bash
python main.py
```

## Resultados

Ao final da execução, o sistema gera:

- Arquivos `.csv` contendo:
  - Texto da notícia
  - Rótulo real (*ground truth*)
  - Predição do modelo
  - Latência da resposta

- Métricas de desempenho:
  - Precisão (*Precision*)
  - Recall
  - F1-Score

- Matrizes de confusão em formato `.png`
