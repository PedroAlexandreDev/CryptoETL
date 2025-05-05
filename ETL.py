import requests
import pandas as pd
from sqlalchemy import create_engine
import logging
import schedule
import time
import json

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def pegarCoins():


    with open("tokens.json", "r") as f:
        data = json.load(f)

    tokens_str = ",".join(data["tokens"])

    try:
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={tokens_str}&vs_currencies=usd")
    except:
        logging.critical("erro nao foi possivel pega os tokens")


    response_coins = response.json()

    logging.info("tokens pegados com sucesso")

    coins = []

    for coin, info in response_coins.items():
        coins.append({
            "name": coin,
            "price": info["usd"]
        })

    df = pd.DataFrame(coins)

    logging.info("feito tabela")

    df.to_csv("coins.csv")

    engine = create_engine('sqlite:///precos_crypto.db')

    df.to_sql('precos', con=engine, if_exists='replace', index=False)


pegarCoins()

schedule.every().day.at("09:40").do(pegarCoins)

while True:
    schedule.run_pending()
    time.sleep(60)
    logging.info("nao ha tarefas")

