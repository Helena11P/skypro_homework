from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

for click in range(5):
    click_button = driver.find_element(
        By.XPATH, '//div[@id="content"]/div/button').click()

delete_button = driver.find_elements(
    By.XPATH, '//*[@id="elements"]/button')

print(f'Количество кнопок "Delete": {len(delete_button)}')

sleep(5)
