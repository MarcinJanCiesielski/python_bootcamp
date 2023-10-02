import smtplib
import datetime as dt
import time
import requests
import secret

def generate_visibility_locations(lat):
    MARGIN = 5
    latitude = int(str(lat).split(".", maxsplit=1)[0])
    return range(latitude - MARGIN, latitude + MARGIN)

def generate_message():
    msg = "Subject:ISS Overhead\n\nLook through the window there is ISS over your head"
    return msg

def get_iss_data():
    response = requests.get("http://api.open-notify.org/iss-now.json", timeout=20)
    response.raise_for_status()
    return response.json()

def get_iss_latitude():
    iss_data = get_iss_data()
    latitude = iss_data["iss_position"]["latitude"]
    lat = int(latitude.split(".")[0])
    print(lat)
    return lat

def is_iss_visible(visibility_range):
    return get_iss_latitude() in visibility_range

def get_sun_data(lng, lat):
    params = {
        "lng": lng,
        "lat": lat,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=params, timeout=20)
    response.raise_for_status()

    return response.json()

def get_sunrise_sunset():
    sun_data = get_sun_data(secret.home_longitude, secret.home_latitude)

    sunrise = sun_data["results"]["sunrise"].split("T")[1].split("+")[0]
    sunset = sun_data["results"]["sunset"].split("T")[1].split("+")[0]

    sunrise_dt = dt.time.fromisoformat(sunrise)
    sunset_dt = dt.time.fromisoformat(sunset)

    return (sunrise_dt, sunset_dt)

def is_night(sunrise, sunset):
    now = dt.datetime.now().time()
    return now < sunrise or now > sunset

def send_email(email, msg):
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=secret.my_email, password=secret.password)
        connection.sendmail(from_addr=secret.my_email, to_addrs=email, msg=msg)


sunrise_time, sunset_time = get_sunrise_sunset()
visibility_locations = generate_visibility_locations(secret.home_latitude)
print()


while True:
    if is_night(sunrise_time, sunset_time) and is_iss_visible(visibility_locations):
        message = generate_message()
        send_email(secret.to_email, message)
        print("message")
    else:
        print("No message")
    time.sleep(60)
