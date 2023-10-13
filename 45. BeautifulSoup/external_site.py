from bs4 import BeautifulSoup
import requests as req

res = req.get("https://news.ycombinator.com/news", timeout=20)
yc_webpage = res.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all("span", class_="titleline")
article_texts = []
article_links = []

for article in articles:
    text = article.a.getText()
    article_texts.append(text)
    link = article.a["href"]
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

largest_number = max(article_upvotes)
most_upvoted = article_upvotes.index(largest_number)

print(article_texts[most_upvoted])
print(article_links[most_upvoted])
