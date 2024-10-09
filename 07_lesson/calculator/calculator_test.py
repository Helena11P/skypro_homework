from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import Calculator


def test_calcultor():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    calculator = Calculator(driver)

    calculator.change_time()
    calculator.click_7()
    calculator.click_plus()
    calculator.click_8()
    calculator.click_equals()
    calculator.wait()
    number = calculator.result()

    assert number == 15

    driver.quit()
