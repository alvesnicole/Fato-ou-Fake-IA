🛡️ Fake News Detection Experiment
Este repositório contém um ambiente de testes para classificação de notícias (Verdadeiro ou Falso) utilizando modelos de Linguagem de Grande Escala (LLMs) via API do Groq.

O experimento foi estruturado para avaliar a precisão e a latência de diferentes modelos ao lidar com informações do cenário brasileiro.

📊 O Dataset
Para este experimento, selecionamos 400 notícias extraídas do dataset Fake.br-Corpus.

Embora tenhamos focado nestas 400 amostras específicas para nossos testes, o código é totalmente compatível com qualquer recorte ou notícia adicional do dataset original.

Controle de Fluxo: O script está configurado para processar 200 notícias por execução. Essa estratégia foi adotada para respeitar rigorosamente os limites de tokens (Rate Limits) e garantir a estabilidade durante as chamadas aos modelos:

llama-3.3-70b-versatile

qwen3-32b

📂 Estrutura do Repositório
Plaintext
├── data_llama-3.3-70b-versatile/   # Resultados gerados pelo Llama 3.3
├── data_qwen3-32b/                 # Resultados gerados pelo Qwen 3
├── data/                           # Pasta contendo as notícias (True/Fake)
├── main.py                         # Script principal de execução
├── engine.py                       # Lógica de comunicação com as APIs
├── .env                            # Variáveis de ambiente (Chaves de API)
└── requirements.txt                # Dependências do projeto

🚀 Como Executar o Projeto
Siga o passo a passo abaixo para configurar o ambiente e rodar o experimento:

1. Clonar e Instalar Dependências
Certifique-se de estar com seu ambiente virtual (venv) ativo. Instale os requisitos necessários:

Bash
pip install -r requirements.txt
2. Configurar Variáveis de Ambiente
adicione sua chave de API do Groq no arquivo nomeado .env, localizado na raíz do projeto.

Snippet de código
GROQ_API_KEY=seu_token_aqui_gsk...
3. Preparar os Dados
Certifique-se de que as notícias do Fake.br-Corpus estejam nas pastas data/true e data/fake conforme configurado no script de carga.

4. Rodar o Experimento
Inicie o processo de classificação executando o script principal:

Bash
python main.py
📈 Resultados
Após a execução, o sistema gerará automaticamente:

Arquivos CSV: Contendo o texto, o rótulo real, a predição do modelo e o tempo de latência.

Métricas: Relatórios de performance (Precisão, Recall e F1-Score) exibidos diretamente no console.
