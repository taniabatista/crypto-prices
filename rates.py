import requests as requests

btc_rates = requests.get("https://shakepay.github.io/programming-exercise/web/rates_CAD_BTC.json").json()
eth_rates = requests.get("https://shakepay.github.io/programming-exercise/web/rates_CAD_ETH.json").json()

rates = {
    'ETH': {rate['createdAt'][:10]: rate['midMarketRate'] for rate in eth_rates},
    'BTC': {rate['createdAt'][:10]: rate['midMarketRate'] for rate in btc_rates},
}
