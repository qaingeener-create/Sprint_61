from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def click_arrow(self, question_number):
        # Предполагаем, что у каждого вопроса есть уникальный селектор для стрелки
        arrow_selector = f".question-{question_number}-arrow"
        arrow = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, arrow_selector)))
        arrow.click()

    def is_text_opened(self, question_number):
        # Проверяем, что текст вопроса открыт
        text_selector = f".question-{question_number}-text"
        return len(self.driver.find_elements(By.CSS_SELECTOR, text_selector)) > 0

    # Локаторы для элементов на главной странице
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, ".top-order-button")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".bottom-order-button")
    SCOOTER_LOGO = (By.ID, "scooter-logo")
    YANDEX_LOGO = (By.ID, "yandex-logo")

    def click_order_button_top(self):
        self.driver.find_element(*self.ORDER_BUTTON_TOP).click()
        return MainPage(self.driver)

    def click_order_button_bottom(self):
        self.driver.find_element(*self.ORDER_BUTTON_BOTTOM).click()
        return MainPage(self.driver)

    def click_scooter_logo_and_check(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()
    # Проверка перехода на главную страницу "Самоката"
    assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Не удалось перейти на главную страницу 'Самоката'"

    def click_yandex_logo_and_check(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()
    # Проверка перехода на главную страницу Дзена
    assert self.driver.current_url.startswith("https://dzen.ru/"), "Не удалось перейти на главную страницу Дзена"
