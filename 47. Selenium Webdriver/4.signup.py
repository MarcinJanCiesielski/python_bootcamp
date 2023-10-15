from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://secure-retreat-92358.herokuapp.com/"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get(URL)

fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
signup_button = driver.find_element(By.CSS_SELECTOR, "button")

fname.send_keys("Grzegorz")

lname.send_keys("Brzęczyszczykiewicz")

email.send_keys('test@test.po')

signup_button.click()
