import requests

response = requests.get("https://shakepay.github.io/programming-exercise/web/transaction_history.json")
data = response.json()
transactions = sorted(data, key=lambda d: d['createdAt'])

balance = {
    "CAD": 0,
    "BTC": 0,
    "ETH": 0
}

for txn in transactions:
    currency = txn['currency']
    amount = txn['amount']

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

    net_worth = balance['CAD'] + balance['BTC']*49567.5 + balance['ETH']*3622.99
    txn['net_worth'] = net_worth
