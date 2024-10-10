from selenium.webdriver.common.by import By
from shop_values import *


class Form:
    def __init__(self, driver):
        self.driver = driver

    def fill_out_form(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(zip)
        self.driver.find_element(
            By.CSS_SELECTOR, "#continue").click()
