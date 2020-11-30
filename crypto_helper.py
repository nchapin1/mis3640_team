import json
from requests import Session

def crypto_current(symbol):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        "start": "1",
        "limit": "5000",
        "convert": "USD",
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "ce4157ad-edeb-4e93-83f0-bb977f31d3e3",
    }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    raw = json.loads(response.text)
    data = raw['data']

    for item in data:
        if item["symbol"] == symbol:
            current = item["quote"]["USD"]["price"]
            break
    return current

def main():
    symbol = str(input())
    result = crypto_current(symbol)
    print(result)

if __name__ == "__main__":
    main()

