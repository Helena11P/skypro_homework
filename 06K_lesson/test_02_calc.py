from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 50)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.maximize_window()

delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
delay_field.clear()
delay_field.send_keys(45)


driver.find_element(
    By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
driver.find_element(
    By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
driver.find_element(
    By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
driver.find_element(
    By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
)

txt = driver.find_element(
    By.CSS_SELECTOR, "div.screen").text
assert txt == "15"
