from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")
sleep(1)
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")
sleep(1)
login_button = driver.find_element(By.CSS_SELECTOR, ".radius").click()
