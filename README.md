# CryptoETL


📊 Projeto ETL de Preços de Criptomoedas

Este projeto realiza a extração diária de preços de criptomoedas via CoinGecko API, transforma os dados em uma tabela estruturada e os armazena em:

    Um arquivo .csv

    Um banco de dados SQLite (precos_crypto.db)

O processo é automatizado com a biblioteca schedule e configurável via JSON.
🚀 Tecnologias Usadas

    Python 3

    requests – Para chamadas HTTP à API

    pandas – Manipulação de dados

    sqlalchemy – Integração com banco SQLite

    schedule – Agendamento automático de tarefas

    logging – Registro de logs de execução

    json – Configuração de tokens

📁 Estrutura do Projeto

etl_cryptopreco/
├── ETL.py              # Script principal
├── tokens.json         # Lista de criptomoedas a monitorar
├── coins.csv           # Exportação dos dados em CSV
├── precos_crypto.db    # Banco de dados SQLite
└── README.md           # Este arquivo

🔧 Como Executar

    Clone este repositório:

git clone https://github.com/seu-usuario/etl_cryptopreco.git
cd etl_cryptopreco

    Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

    Instale as dependências:

pip install -r requirements.txt

    Caso não tenha um requirements.txt, use:

pip install requests pandas sqlalchemy schedule

    Edite o arquivo tokens.json com as moedas desejadas:

{
  "tokens": ["bitcoin", "ethereum", "solana", "monero"]
}

    Execute o script:

python ETL.py

🧠 O que o script faz

    Lê as moedas do tokens.json

    Consulta seus preços na API da CoinGecko

    Gera uma tabela com name e price

    Salva a tabela em CSV e em SQLite

    Agenda a execução automática diariamente às 09:40

🗃 Exemplo de saída (tabela gerada)
name	price
bitcoin	95369
ethereum	1824.86
solana	146.84
monero	277.57
✅ Próximos passos (ideias)

    Armazenar com timestamps

    Exportar para nuvem (Google BigQuery, S3 etc.)

    Integrar com Airflow

    Criar dashboard com Streamlit
