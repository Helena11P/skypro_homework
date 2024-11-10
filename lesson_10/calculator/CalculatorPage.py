from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calculator:

    """
    В этом классе методы для работы на странице калькулятора
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    @allure.step("Изменить время ожидания результата")
    def change_time(self, time: int) -> None:
        """
        Метод очищает поле с числом и добавляет новое время, переданое в параметре time
        """
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(time)

    @allure.step("Нажать на кнопку 7")
    def click_7(self) -> None:
        """
        Нажимает на кнопку 7
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()

    @allure.step("Нажать на +")
    def click_plus(self) -> None:
        """
        Нажимает на кнопку +
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()

    @allure.step("Нажать на 8")
    def click_8(self) -> None:
        """
        Нажимает на кнопку 8
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()

    @allure.step("Нажать на =")
    def click_equals(self) -> None:
        """
        Нажимает на =
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    @allure.step("Подождать появления результата в поле калькулятора")
    def wait(self) -> None:
        """
        Ждет появления результата в поле калькулятора
        """
        waiter = WebDriverWait(self.driver, 50)
        waiter.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, "div.screen"), "15"))

    @allure.step("Посмотреть результат")
    def result(self) -> int:
        """
        Возвращает результат полученный при использовании калькулятора
        """
        result = self.driver.find_element(
            By.CSS_SELECTOR, "div.screen").text
        return int(result)
