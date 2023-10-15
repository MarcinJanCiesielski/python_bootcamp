from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/events/"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(URL)

dates = driver.find_elements(By.CSS_SELECTOR, "p time")
names = driver.find_elements(By.CSS_SELECTOR, ".event-title a")

events_dict = {}

for index, (date, name) in enumerate(zip(dates, names)):
    events_dict[index] = {
        "time": date.text,
        "name": name.text,
    }

print(events_dict)

driver.quit()
