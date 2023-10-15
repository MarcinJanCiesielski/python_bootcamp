from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.amazon.pl/Google-Pixel-odblokowany-obiektywem-szerokok%C4%85tnym/dp/B0BDK63RF3?th=1"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
search_bar = driver.find_element(By.ID, "twotabsearchtextbox")

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map]/div[2]/div/ul/li[3]/a')

print(search_bar)
# driver.quit()
