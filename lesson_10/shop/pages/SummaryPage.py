from selenium.webdriver.common.by import By
import allure


class TotalPrice:
    """
    Содержит метод для оценки окончательной стоимости
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Посмотреть общую стоимость")
    def total(self) -> str:
        """
        Находит общую сумму и возвращает ее
        """
        result = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        total_price = result.strip().replace("Total: $", "")
        print(f"Общая сумма = ${total_price}")
        return total_price
