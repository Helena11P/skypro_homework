from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/entry_ad")

sleep(2)
close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer")
close_button.click()

sleep(5)
