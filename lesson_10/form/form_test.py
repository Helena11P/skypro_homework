from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from FormPage import FillOutForm
from values import red_field, green_field
import allure


@allure.title("Заполнение формы")
@allure.description(
    "Заполяет все поля, кроме 'Zip', данными. Проверяет, что поле 'Zip' подсвечено красным цветом, а остальные зеленым")
@allure.feature("INPUT")
@allure.severity("blocker")
def test_field_class():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    fill_out_form = FillOutForm(driver)
    fill_out_form.add_value()
    fill_out_form.click_button()
    with allure.step(f"Проверить, что класс поля zip содержит слово {red_field}"):
        assert red_field in fill_out_form.zip_class()
    with allure.step(f"Проверить, что класс поля first name содержит слово {green_field}"):
        assert green_field in fill_out_form.first_name_class()
    with allure.step(f"Проверить, что класс поля last name содержит слово {green_field}"):
        assert green_field in fill_out_form.last_name_class()
    with allure.step(f"Проверить, что класс поля address содержит слово {green_field}"):
        assert green_field in fill_out_form.address_class()
    with allure.step(f"Проверить, что класс поля city содержит слово {green_field}"):
        assert green_field in fill_out_form.city_class()
    with allure.step(f"Проверить, что класс поля country содержит слово {green_field}"):
        assert green_field in fill_out_form.country_class()
    with allure.step(f"Проверить, что класс поля email содержит слово {green_field}"):
        assert green_field in fill_out_form.email_class()
    with allure.step(f"Проверить, что класс поля phone содержит слово {green_field}"):
        assert green_field in fill_out_form.phone_class()
    with allure.step(f"Проверить, что класс поля job position содержит слово {green_field}"):
        assert green_field in fill_out_form.job_position_class()
    with allure.step(f"Проверить, что класс поля company содержит слово {green_field}"):
        assert green_field in fill_out_form.company_class()

    driver.quit()
