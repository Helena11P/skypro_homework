from selenium.webdriver.common.by import By
from values import *


class FillOutForm:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    def add_value(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=first-name]").send_keys(first_name)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=last-name]").send_keys(last_name)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=address]").send_keys(address)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=e-mail]").send_keys(email)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=phone]").send_keys(phone_number)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=city]").send_keys(city)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=country]").send_keys(country)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=job-position]").send_keys(
                job_position)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=company]").send_keys(company)

    def click_button(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type=submit]").click()

    def zip_class(self):
        zip_class = self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code").get_attribute("class")
        return zip_class

    def first_name_class(self):
        first_name_class = self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").get_attribute("class")
        return first_name_class

    def last_name_class(self):
        last_name_class = self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").get_attribute("class")
        return last_name_class

    def address_class(self):
        address_class = self.driver.find_element(
            By.CSS_SELECTOR, "#address").get_attribute("class")
        return address_class

    def city_class(self):
        city_class = self.driver.find_element(
            By.CSS_SELECTOR, "#city").get_attribute("class")
        return city_class

    def country_class(self):
        country_class = self.driver.find_element(
            By.CSS_SELECTOR, "#country").get_attribute("class")
        return country_class

    def email_class(self):
        email_class = self.driver.find_element(
            By.CSS_SELECTOR, "#e-mail").get_attribute("class")
        return email_class

    def phone_class(self):
        phone_class = self.driver.find_element(
            By.CSS_SELECTOR, "#phone").get_attribute("class")
        return phone_class

    def job_position_class(self):
        job_position_class = self.driver.find_element(
            By.CSS_SELECTOR, "#job-position").get_attribute("class")
        return job_position_class

    def company_class(self):
        company_class = self.driver.find_element(
            By.CSS_SELECTOR, "#company").get_attribute("class")
        return company_class
