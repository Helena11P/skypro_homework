from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddToCart:

    def __init__(self, driver):
        self.driver = driver

    def add_Sauce_Labs_Backpack(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    def add_Sauce_Labs_Bolt_TShirt(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_Sauce_Labs_Onesie(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()
        waiter = WebDriverWait(self.driver, 10)
        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout")))
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
