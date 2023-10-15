from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


URL = "https://en.wikipedia.org/wiki/Main_Page"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get(URL)
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

print(article_count.text)

# article_count.click()

# pages = driver.find_element(By.LINK_TEXT, "Pages")
# pages.click()

search = driver.find_element(By.NAME, "search")

search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()
