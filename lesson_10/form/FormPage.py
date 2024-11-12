from selenium.webdriver.common.by import By
from values import *
import allure


class FillOutForm:
    """
    Содержит методы для работы с формой
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    @allure.step("Добавить во все поля, кроме Zip, данные")
    def add_value(self) -> None:
        """
        Добавляет в поля данные, которые находятся в values.py
        """
        with allure.step(f"Добавит {first_name} в поле first name"):
            self.driver.find_element(
                By.CSS_SELECTOR, "input[name=first-name]").send_keys(first_name)
        with allure.step(f"Добавит {last_name} в поле last name"):
            self.driver.find_element(
                By.CSS_SELECTOR, "input[name=last-name]").send_keys(last_name)
        with allure.step(f"Добавит {address} в поле address"):
            self.driver.find_element(
                By.CSS_SELECTOR, "input[name=address]").send_keys(address)
        with allure.step(f"Добавит {email} в поле email"):
            self.driver.find_element(
                By.CSS_SELECTOR, "input[name=e-mail]").send_keys(email)
        with allure.step(f"Добавит {phone_number} в поле phone number"):
            self.driver.find_element(
                By.CSS_SELECTOR, "input[name=phone]").send_keys(phone_number)
        with allure.step(f"Добавит {city} в поле city "):
            self.driver.find_element(
                By.CSS_SELECTOR, "input[name=city]").send_keys(city)
        with allure.step(f"Добавит {country} в поле country"):
            self.driver.find_element(
                By.CSS_SELECTOR, "input[name=country]").send_keys(country)
        with allure.step(f"Добавит {job_position} в поле job position"):
            self.driver.find_element(
                By.CSS_SELECTOR, "input[name=job-position]").send_keys(job_position)
        with allure.step(f"Добавит {company} в поле company"):
            self.driver.find_element(
                By.CSS_SELECTOR, "input[name=company]").send_keys(company)

    @allure.step("Нажать на кнопку Submit")
    def click_button(self) -> None:
        """
        Нажимает на кнопку Submit
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type=submit]").click()

    @allure.step("Посмотреть класс подсвеченного поля zip")
    def zip_class(self) -> str:
        """
        Находит класс подсвеченного поля Zip и возвращает его
        """
        zip_class = self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code").get_attribute("class")
        return zip_class

    @allure.step("Посмотреть класс подсвеченного поля first name")
    def first_name_class(self) -> str:
        """
        Находит класс подсвеченного поля first name и возвращает его
        """
        first_name_class = self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").get_attribute("class")
        return first_name_class

    @allure.step("Посмотреть класс подсвеченного поля last name")
    def last_name_class(self) -> str:
        """
        Находит класс подсвеченного поля last name и возвращает его
        """
        last_name_class = self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").get_attribute("class")
        return last_name_class

    @allure.step("Посмотреть класс подсвеченного поля address")
    def address_class(self) -> str:
        """
        Находит класс подсвеченного поля address и возвращает его
        """
        address_class = self.driver.find_element(
            By.CSS_SELECTOR, "#address").get_attribute("class")
        return address_class

    @allure.step("Посмотреть класс подсвеченного поля city")
    def city_class(self) -> str:
        """
        Находит класс подсвеченного поля city и возвращает его
        """
        city_class = self.driver.find_element(
            By.CSS_SELECTOR, "#city").get_attribute("class")
        return city_class

    @allure.step("Посмотреть класс подсвеченного поля country")
    def country_class(self) -> str:
        """
        Находит класс подсвеченного поля country и возвращает его
        """
        country_class = self.driver.find_element(
            By.CSS_SELECTOR, "#country").get_attribute("class")
        return country_class

    @allure.step("Посмотреть класс подсвеченного поля email")
    def email_class(self) -> str:
        """
        Находит класс подсвеченного поля email и возвращает его
        """
        email_class = self.driver.find_element(
            By.CSS_SELECTOR, "#e-mail").get_attribute("class")
        return email_class

    @allure.step("Посмотреть класс подсвеченного поля phone number")
    def phone_class(self) -> str:
        """
        Находит класс подсвеченного поля phone number и возвращает его
        """
        phone_class = self.driver.find_element(
            By.CSS_SELECTOR, "#phone").get_attribute("class")
        return phone_class

    @allure.step("Посмотреть класс подсвеченного поля job position")
    def job_position_class(self) -> str:
        """
        Находит класс подсвеченного поля job position и возвращает его
        """
        job_position_class = self.driver.find_element(
            By.CSS_SELECTOR, "#job-position").get_attribute("class")
        return job_position_class

    @allure.step("Посмотреть класс подсвеченного поля company")
    def company_class(self) -> str:
        """
        Находит класс подсвеченного поля company и возвращает его
        """
        company_class = self.driver.find_element(
            By.CSS_SELECTOR, "#company").get_attribute("class")
        return company_class
