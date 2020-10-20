import requests

response = requests.get("http://trojmiasto.pl/juhu")

try:
    response.raise_for_status()
except Exception as e:
    print("Wystapil blad:", e)
finally:
    print(response.status_code)

