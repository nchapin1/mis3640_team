def get_crypto_marekt_price(symbol):

    from requests import Request, Session
    from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
    import json
    import pprint

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        "start": "1",
        "limit": "1",
        "convert": "USD",
    }  # --> if we want the price in other currency
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "ce4157ad-edeb-4e93-83f0-bb977f31d3e3",
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    all_crypto_info = data["data"]
    # print(type(all_crypto_info))  # this is a list
    for each_crypto in all_crypto_info:
        if each_crypto["symbol"] == symbol:
            market_price = each_crypto["quote"]["USD"]["price"]
            # market_price = f"{raw_market_price:.2f}"
            return market_price

print(get_crypto_marekt_price('btc'))