import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line đź‘‡
response = requests.get(url=URL, timeout=20)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

title_tags = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in title_tags]

titles = movie_titles[::-1]

with open("100_movies.txt", mode="w", encoding="utf8") as f:
    for line in titles:
        f.writelines(f"{line}\n")

