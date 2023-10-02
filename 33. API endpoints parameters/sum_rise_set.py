import requests
import secret

params = {
    "lng": secret.home_longitude,
    "lat": secret.home_latitude,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=params, timeout=20)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"].split("T")[1].split("+")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split("+")[0]

print(sunrise)
print(sunset)
