from selenium.webdriver.common.by import By


class TotalPrice:
    def __init__(self, driver):
        self.driver = driver

    def total(self):
        result = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        total_price = result.strip().replace("Total: $", "")
        print(f"Общая сумма = ${total_price}")
        return total_price
