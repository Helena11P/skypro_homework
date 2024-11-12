from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import Calculator
import allure


@allure.title("Калькулятор")
@allure.description(
    "Тестирует калькулятор: нажимает на кнопки, ждет результат, сравнивает полученный результат с ожидаемым")
@allure.feature("COUNT")
@allure.severity("blocker")
def test_calcultor():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    calculator = Calculator(driver)

    calculator.change_time(45)
    calculator.click_7()
    calculator.click_plus()
    calculator.click_8()
    calculator.click_equals()
    calculator.wait()
    number = calculator.result()
    with allure.step("Сравнить полученый результат с ожидаемым"):
        assert number == 15

    driver.quit()
