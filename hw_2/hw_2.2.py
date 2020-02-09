from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH,"//a[text()='Help']").click()

search = driver.find_element(By.NAME, 'help_keywords')
search.clear()
search.send_keys('cancel order')

driver.find_element(By.XPATH,"//div[@class='a-column a-span2 a-span-last']").click()

assert 'Cancel Items or Orders' in driver.find_element(By.XPATH,

"//div[contains(@class,'help-content')]/h1").text

driver.quit()
