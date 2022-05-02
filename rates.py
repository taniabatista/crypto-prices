import requests as requests

btc_rates = requests.get("https://shakepay.github.io/programming-exercise/web/rates_CAD_BTC.json").json()
eth_rates = requests.get("https://shakepay.github.io/programming-exercise/web/rates_CAD_ETH.json").json()

rates = {
    'ETH': {rate['createdAt'][:10]: rate['midMarketRate'] for rate in eth_rates},
    'BTC': {rate['createdAt'][:10]: rate['midMarketRate'] for rate in btc_rates},
}


def get_rate(currency, date):

    try:
        return rates[currency][date]

    except KeyError:
        entries = 0
        total = 0
        for k, v in rates[currency].items():
            if k.startswith(date[:9]):
                entries += 1
                total += float(v)
                return total/entries
            elif k.startswith(date[:7]):
                entries += 1
                total += float(v)
                return total/entries
            elif k.startswith(date[:5]):
                entries += 1
                total += float(v)
                return total/entries
