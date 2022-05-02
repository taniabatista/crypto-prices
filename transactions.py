import requests

response = requests.get("https://shakepay.github.io/programming-exercise/web/transaction_history.json")
data = response.json()
data = sorted(data, key=lambda d: d['createdAt'])
