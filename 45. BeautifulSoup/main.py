from bs4 import BeautifulSoup
# import lxml


with open("./website.html", "r", encoding="utf8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

h1_heading = soup.find(name="h1", id="name")

h3_heading = soup.find(name="h3", class_="heading")

company_url = soup.select_one(selector="p a")
company_url = soup.select_one(selector="#name")

headings = soup.select(selector=".heading")

print(headings)
