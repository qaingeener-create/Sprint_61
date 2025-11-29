from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def open(self):
        # код для открытия страницы
        pass

    def click_arrow(self, question_number):
        # код для клика по стрелке вопроса
        pass

    def is_text_opened(self, question_number):
        # код для проверки, открылся ли текст вопроса
        pass

    # Локаторы для элементов на главной странице
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, ".top-order-button")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".bottom-order-button")
    SCOOTER_LOGO = (By.ID, "scooter-logo")
    YANDEX_LOGO = (By.ID, "yandex-logo")

    def open(self):
        # Метод для открытия главной страницы
        pass

    def click_order_button_top(self):
        self.driver.find_element(*self.ORDER_BUTTON_TOP).click()
        return OrderPage(self.driver)

    def click_order_button_bottom(self):
        self.driver.find_element(*self.ORDER_BUTTON_BOTTOM).click()
        return OrderPage(self.driver)

    def click_scooter_logo_and_check(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()
        # Проверка перехода на главную страницу "Самоката"
        pass

    def click_yandex_logo_and_check(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()
        # Проверка перехода на главную страницу Дзена
        pass