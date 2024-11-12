from selenium.webdriver.common.by import By
from shop_values import *
import allure


class Form:
    """
    Содержит метод для работы с формой оформления заказа
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнить форму заказа")
    def fill_out_form(self) -> None:
        """
        Заполняет форму оформления заказа данными, которые находятся в shop_values.py
        """
        with allure.step(f"Добавить {first_name} в поле first name"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        with allure.step(f"Добавить {last_name} в поле last name"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        with allure.step(f"Добавить {zip} в поле zip/postal code"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#postal-code").send_keys(zip)
        with allure.step("Нажать кнопку continue"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#continue").click()
