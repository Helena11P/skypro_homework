from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 40)
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

waiter.until(
     EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
 )
txt = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)
