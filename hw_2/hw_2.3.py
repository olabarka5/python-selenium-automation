from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

orders = driver.find_element(By.XPATH, "//a[@id='nav-orders']")
orders.click()

sleep(1)

sign_in_header = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
assert 'Sign-In' == sign_in_header.text

driver.quit()


