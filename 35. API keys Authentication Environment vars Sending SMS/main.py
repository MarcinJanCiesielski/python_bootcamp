import smtplib
import os
import requests
import secret

OPENWEATHERMAP_API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")

def generate_message():
    msg = "Subject:I will rain!\n\nTake an umbrella!"
    return msg

def send_email(email, msg):
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=secret.my_email, password=secret.password)
        connection.sendmail(from_addr=secret.my_email, to_addrs=email, msg=msg)


def get_openweathermap_data(lat, lnt):

    params = {
        "lat": lat,
        "lon": lnt,
        "appid": OPENWEATHERMAP_API_KEY,
        "exclude":"current,minutely,daily"
    }
    API_URL = "https://api.openweathermap.org/data/2.5/onecall"

    response = requests.get(url=API_URL, params=params, timeout=20)
    response.raise_for_status()
    return response.json()

def will_it_rain_in_12h():
    rain = False
    weather_data = get_openweathermap_data(secret.home_latitude, secret.home_longitude)

    weather_12h = weather_data["hourly"][:12]
    for hour in weather_12h:
        condition_id = int(hour["weather"][0]["id"])
        if condition_id < 700:
            rain = True

    return rain

if will_it_rain_in_12h():
    message = generate_message()
    print(message)
    send_email(secret.to_email, message)
