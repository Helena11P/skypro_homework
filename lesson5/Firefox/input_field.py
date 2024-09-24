from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.CSS_SELECTOR, "input[type = number]")
input_field.send_keys('100')
sleep(1)
input_field.clear()
sleep(1)
input_field.send_keys('999')

sleep(3)
