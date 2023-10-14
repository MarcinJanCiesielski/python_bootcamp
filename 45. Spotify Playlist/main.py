from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=url, timeout=20)
response.raise_for_status()

html = response.text

soup = BeautifulSoup(html, "html.parser")
titles = [title.getText().strip() for title in soup.select(selector="li ul li h3")]

print(titles)
