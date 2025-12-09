from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Установим время ожидания по умолчанию

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
