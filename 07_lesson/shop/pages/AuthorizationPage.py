from selenium.webdriver.common.by import By
from shop_values import *


class Authorization():

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def add_values(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
