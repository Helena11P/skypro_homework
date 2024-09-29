from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
field.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

print(button.text)
