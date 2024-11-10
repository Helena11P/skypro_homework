from selenium.webdriver.common.by import By
from shop_values import *
import allure


class Authorization():
    """
    Содержит метод для работы с формой авторизации
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    @allure.step("Добавить данные в форму авторизации")
    def add_values(self) -> None:
        """
        Добавляется данные в поля авторизации (данные находятся в файле shop_values) и нажимает на кнопку Login
        """
        with allure.step(f"Добавить логин {username}"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#user-name").send_keys(username)
        with allure.step(f"Добавить пароль {password}"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#password").send_keys(password)
        with allure.step("Нажать кнопку login"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#login-button").click()
