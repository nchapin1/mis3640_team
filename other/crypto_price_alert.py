def get_crypto_marekt_price(crypto_tracked):

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
        if each_crypto["name"] == crypto_tracked:
            market_price = each_crypto["quote"]["USD"]["price"]
            # market_price = f"{raw_market_price:.2f}"

    return market_price


# print(get_crypto_marekt_price("Bitcoin"))


class Cryptoprice:
    def __init__(self, crypto_name, purchased_price, target_return, max_loss):
        """
        crypto_name --> user input; purchased_price --> user input; market_price --> data extraction; target_return --> user input; max_loss --> user input
        """
        self.crypto_name = crypto_name
        self.purchased_price = purchased_price
        self.target_return = target_return
        self.max_loss = max_loss

    def alert_activation(self):
        loss_alert = self.purchased_price * (1 - self.max_loss)
        # print(type(loss_alert)) ---> float
        sell_reminder = self.purchased_price * (1 + self.target_return)
        if get_crypto_marekt_price(self.crypto_name) < loss_alert:
            return True
        elif get_crypto_marekt_price(self.crypto_name) >= sell_reminder:
            return True
        else:
            return False

    def send_message(self, loss_alert):  # use a method as a parameter?
        if alert_activation(self) == True:
            pass
            # send a message


crypto1 = Cryptoprice("Bitcoin", 10000, 0.1, 0.05)
# print(type(get_crypto_marekt_price(crypto1.crypto_name)))
print(Cryptoprice.alert_activation(crypto1))
# print(type(crypto1.))
# print(crypto1.target_return)