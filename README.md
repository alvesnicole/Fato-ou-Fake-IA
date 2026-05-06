# Fake News Detection Experiment

Este repositório contém um ambiente de testes para classificação de notícias (**Verdadeiro** ou **Falso**) utilizando Modelos de Linguagem de Grande Escala (LLMs) via API do **Groq**.

O experimento foi estruturado para avaliar a precisão e a latência de diferentes modelos ao lidar com informações do cenário brasileiro.

## 📊 O Dataset

Para este experimento, selecionamos **400 notícias** extraídas do dataset *Fake.br-Corpus*.

Embora tenhamos focado nestas 400 amostras específicas para nossos testes, o código é totalmente compatível com qualquer recorte ou notícia adicional do dataset original.

### Controle de Fluxo

O script está configurado para processar **200 notícias por execução**. Essa estratégia foi adotada para respeitar rigorosamente os limites de tokens (*Rate Limits*) e garantir a estabilidade durante as chamadas aos modelos:

- `llama-3.3-70b-versatile`
- `qwen3-32b`

---

## 📂 Estrutura do Projeto

```plaintext
├── data_llama-3.3-70b-versatile/
│   ├── data/                       # Diretório contendo as notícias
│   ├── results/                    # Diretório onde os resultados serão gerados
│   ├── .env                        # Configuração da chave da API
│   ├── config.py                   # Configurações gerais do experimento
│   ├── data_loader.py              # Carregamento e organização dos dados
│   ├── engine.py                   # Interface de comunicação com a API
│   └── main.py                     # Execução principal do experimento
│
├── data_qwen3-32b/
│   ├── data/                       # Diretório contendo as notícias
│   ├── results/                    # Diretório onde os resultados serão gerados
│   ├── .env                        # Configuração da chave da API
│   ├── config.py                   # Configurações gerais do experimento
│   ├── data_loader.py              # Carregamento e organização dos dados
│   ├── engine.py                   # Interface de comunicação com a API
│   └── main.py                     # Execução principal do experimento
│
└── README.md
```

## 🚀 Instalação

Ative seu ambiente virtual (`venv`) e instale as dependências:

```bash
pip install -r requirements.txt
```

## 🔑 Configuração da API

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
```

## ▶️ Execução

Execute o experimento com:

```bash
python main.py
```

## 📈 Resultados

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
