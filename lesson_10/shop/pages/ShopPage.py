from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AddToCart:
    """
    Содержит методы для добавления товаров в корзину
    """

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавить Sauce Labs Backpack в корзину")
    def add_Sauce_Labs_Backpack(self) -> None:
        """
        Добавляет Sauce Labs Backpack в корзину
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    @allure.step("Добавить Sauce Labs Bolt T-Shirt в корзину")
    def add_Sauce_Labs_Bolt_TShirt(self) -> None:
        """
        Добавляет Sauce Labs Bolt T-Shirt в корзину
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    @allure.step("Добавить Sauce Labs Onesie в корзину")
    def add_Sauce_Labs_Onesie(self) -> None:
        """
        Добавляет Sauce Labs Onesie в корзину
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    @allure.step("Перейти в корзину и открыть форму оформления заказа")
    def go_to_cart(self) -> None:
        """
        Нажимает на кнопку корзины, ожидает открытия корзины и переходит в форму оформления заказа
        """
        with allure.step("Нажать кнопку корзины"):
            self.driver.find_element(
                By.CSS_SELECTOR, "a.shopping_cart_link").click()
        with allure.step("Дождаться открытия корзины"):
            waiter = WebDriverWait(self.driver, 10)
            waiter.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout")))
        with allure.step("Нажать кнопку checkout"):
            self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
