import requests
from rates import get_rate

response = requests.get("https://shakepay.github.io/programming-exercise/web/transaction_history.json")
data = response.json()
transactions = sorted(data, key=lambda d: d['createdAt'])

balance = {
    "CAD": 0,
    "BTC": 0,
    "ETH": 0
}

net_worth_by_day = {}
for txn in transactions:
    currency = txn['currency']
    amount = txn['amount']
    date = txn['createdAt'][:10]

    if txn['direction'] == 'debit':
        balance[currency] -= amount

    if txn['direction'] == 'credit':
        balance[currency] += amount

    if txn['direction'] is None:
        balance[currency] -= amount

        to_currency = txn['to']['currency']
        to_amount = txn['to']['amount']
        balance[to_currency] += to_amount

    txn['balance'] = balance

    net = (
            balance['CAD'] +
            (balance['BTC'] * get_rate('BTC', date)) +
            (balance['ETH'] * get_rate('ETH', date))
    )/1000000
    net_worth = float(format(net, ".3f"))

    txn['net_worth'] = net_worth
    net_worth_by_day.update({date: net_worth})
