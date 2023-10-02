import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=20)

response.raise_for_status()

print(response.json())

position = response.json()["iss_position"]

print(position)
