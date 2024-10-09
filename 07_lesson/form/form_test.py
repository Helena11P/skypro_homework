from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from FormPage import FillOutForm
from values import red_field, green_field


def test_field_class():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    fill_out_form = FillOutForm(driver)
    fill_out_form.add_value()
    fill_out_form.click_button()
    assert red_field in fill_out_form.zip_class()
    assert green_field in fill_out_form.first_name_class()
    assert green_field in fill_out_form.last_name_class()
    assert green_field in fill_out_form.address_class()
    assert green_field in fill_out_form.city_class()
    assert green_field in fill_out_form.country_class()
    assert green_field in fill_out_form.email_class()
    assert green_field in fill_out_form.phone_class()
    assert green_field in fill_out_form.job_position_class()
    assert green_field in fill_out_form.company_class()

    driver.quit()
