import requests

BASE_API_URL = "https://opentdb.com/api.php"
params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url=BASE_API_URL, params=params, timeout=20)
response.raise_for_status()

question_data = response.json()["results"]
