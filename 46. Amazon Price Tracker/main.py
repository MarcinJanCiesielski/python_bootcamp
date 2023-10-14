from bs4 import BeautifulSoup
import requests
import notification_manager
import secret

URL = "https://www.amazon.pl/Google-Pixel-odblokowany-obiektywem-szerokok%C4%85tnym/dp/B0BDK63RF3?th=1"
PURCHASE_LEVEL = 1999

nm = notification_manager.NotificationManager()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "pl,en-US;q=0.9,en;q=0.8,en-GB;q=0.7"
}

response = requests.get(url=URL, headers=headers, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

price = float(soup.find(class_="a-offscreen").get_text().replace('\xa0', "").replace(",", ".")[:-2])

if price <= PURCHASE_LEVEL:
    message = nm.prepare_message("Google Pixel 7", price)
    nm.send_emails(message,secret.to_email)
