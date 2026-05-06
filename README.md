Fake News Detection Experiment
Este repositório apresenta um ambiente de testes para a classificação automatizada de notícias (Verdadeiro vs. Falso) utilizando Modelos de Linguagem de Grande Escala (LLMs) via infraestrutura da API Groq. O objetivo do projeto é avaliar a acurácia e a latência de modelos de ponta no processamento de informações no contexto brasileiro.

Dataset e Metodologia
Amostragem: Foram selecionadas 400 notícias extraídas do dataset Fake.br-Corpus.

Compatibilidade: O código é modular e totalmente compatível com qualquer volume de dados ou recortes adicionais do dataset original.

Controle de Fluxo: Para garantir a estabilidade das requisições e respeitar os limites de taxa (Rate Limits) e janelas de tokens das APIs, o script está configurado para processar 200 notícias por execução.

Modelos Avaliados
llama-3.3-70b-versatile

qwen3-32b

Estrutura do Repositório
Plaintext
├── data_llama-3.3-70b-versatile/   # Resultados e logs do modelo Llama 3.3
├── data_qwen3-32b/                 # Resultados e logs do modelo Qwen 3
├── data/                           # Diretório de origem (Subpastas /true e /fake)
├── main.py                         # Orquestrador principal do experimento
├── engine.py                       # Interface de comunicação com as APIs
├── .env                            # Configuração de chaves de acesso
└── requirements.txt                # Dependências de software
Guia de Instalação e Execução
Siga as etapas abaixo para configurar o ambiente local:

1. Preparação do Ambiente
Certifique-se de que seu ambiente virtual (venv) está ativo e instale as dependências necessárias:

Bash
pip install -r requirements.txt
2. Configuração de Credenciais
Crie um arquivo .env na raiz do projeto e insira sua chave de API do Groq:

Snippet de código
GROQ_API_KEY=sua_chave_aqui
3. Organização dos Dados
As notícias devem estar organizadas no diretório data/, separadas nas subpastas true/ e fake/, seguindo o padrão de nomenclatura do Fake.br-Corpus.

4. Execução do Experimento
Inicie o processamento dos dados através do comando:

Bash
python main.py
Resultados Gerados
Ao final da execução, o sistema exporta os seguintes dados:

Arquivos CSV: Consolidação contendo o texto da notícia, rótulo real (ground truth), predição do modelo e latência exata da resposta.

Relatórios de Performance: Exibição imediata no console das métricas de classificação, incluindo Precisão, Recall e F1-Score.
