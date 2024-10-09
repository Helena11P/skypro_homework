from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.AuthorizationPage import Authorization
from pages.ShopPage import AddToCart
from pages.FormShopPage import Form
from pages.SummaryPage import TotalPrice


def test_shop():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    authorization = Authorization(driver)
    authorization.add_values()

    add_to_cart = AddToCart(driver)
    add_to_cart.add_Sauce_Labs_Backpack()
    add_to_cart.add_Sauce_Labs_Bolt_TShirt()
    add_to_cart.add_Sauce_Labs_Onesie()
    add_to_cart.go_to_cart()

    form = Form(driver)
    form.fill_out_form()

    total_price = TotalPrice(driver)
    sum = total_price.total()

    driver.quit()

    assert sum == "58.29"
