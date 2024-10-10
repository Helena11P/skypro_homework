from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    def change_time(self):
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(45)

    def click_7(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()

    def click_plus(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()

    def click_8(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()

    def click_equals(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def wait(self):
        waiter = WebDriverWait(self.driver, 50)
        waiter.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, "div.screen"), "15"))

    def result(self):
        result = self.driver.find_element(
            By.CSS_SELECTOR, "div.screen").text
        return int(result)
