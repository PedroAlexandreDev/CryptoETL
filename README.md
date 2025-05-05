# CryptoETL

# Projeto ETL de Preços de Criptomoedas

Este projeto realiza a extração diária de preços de criptomoedas via [CoinGecko API](https://www.coingecko.com/), transforma os dados em uma tabela estruturada e os armazena em:

- Um arquivo `.csv`
- Um banco de dados SQLite (`precos_crypto.db`)

O processo é automatizado com a biblioteca `schedule` e configurável via JSON.

---

## 🚀 Tecnologias Usadas

- `Python 3`
- `requests` – Para chamadas HTTP à API
- `pandas` – Manipulação de dados
- `sqlalchemy` – Integração com banco SQLite
- `schedule` – Agendamento automático de tarefas
- `logging` – Registro de logs de execução
- `json` – Configuração de tokens

---

## 📁 Estrutura do Projeto

etl_cryptopreco/
├── ETL.py # Script principal
├── tokens.json # Lista de criptomoedas a monitorar
├── coins.csv # Exportação dos dados em CSV
├── precos_crypto.db # Banco de dados SQLite
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo


---

## 🔧 Como Executar

1. Clone este repositório:

```bash
https://github.com/PedroAlexandreDev/CryptoETL.git
cd etl_cryptopreco
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Edite o arquivo tokens.json com as moedas desejadas:

```bash
{
  "tokens": ["bitcoin", "ethereum", "solana", "monero"]
}
```

5. Execute o script:
   
```bash
python ETL.py
```

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

📝 Licença

Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.


---

### Como organizar tudo:

1. Crie um arquivo chamado `requirements.txt` no seu repositório e adicione as dependências nele.
2. Crie ou edite o arquivo `README.md` no seu repositório com o conteúdo acima.


