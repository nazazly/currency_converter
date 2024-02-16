import requests

API_KEY = 'fca_live_Q3qPte1loHt7w5s5VXl165g67y8oVTzU8NygzJVr'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["SGD", "USD", "CAD", "EUR", "AUD", "MYR"]

def convert_currency(base):
    # break down currencies into a string with ','
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency.")
        return None
    
while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for key, value in data.items():
        print(f"{key}: {value}")