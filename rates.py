import requests as requests


btc_rates = requests.get("https://shakepay.github.io/programming-exercise/web/rates_CAD_BTC.json").json()
eth_rates = requests.get("https://shakepay.github.io/programming-exercise/web/rates_CAD_ETH.json").json()


rates = {
    'ETH': {rate['createdAt'][:10]: rate['midMarketRate'] for rate in eth_rates},
    'BTC': {rate['createdAt'][:10]: rate['midMarketRate'] for rate in btc_rates},
}


btc_dates = list(rates['BTC'].keys())
eth_dates = list(rates['ETH'].keys())


def get_rate(currency, date):

    try:
        return rates[currency][date]

    # if rate doesn't exist for a transaction's date, then return the next rate
    except KeyError:

        if currency == 'BTC':
            lst = list(rates['BTC'].keys())
            lst.append(date)
            tmr_index = sorted(lst).index(date) + 1
            date = btc_dates[tmr_index]
            return rates['BTC'][date]

        if currency == 'ETH':
            lst = list(rates['ETH'].keys())
            lst.append(date)
            srted_lst = sorted(lst)
            tmr_index = srted_lst.index(date) + 1
            date = eth_dates[tmr_index]
            return rates['ETH'][date]
