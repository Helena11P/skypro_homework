from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")


try:
    blue_button = driver.find_element(
        By.XPATH, '//div[@class="container"]/button').click()
    print("Success")
except ():
    print("Failure")


sleep(1)
