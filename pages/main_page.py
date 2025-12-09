from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        self.scroll_into_view()  # Прокручиваем страницу сразу после открытия

    def scroll_into_view(self):
    #Прокручивает страницу так, чтобы нужный элемент стал видимым.
        element = self.driver.find_element(By.XPATH, '//div[contains(@class, "Home_FAQ")]')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)  # Приостанавливает выполнение на 1 секунду
        
    def open_all_questions(self):
        for i in range(8):  # Предполагаем, что у нас есть 8 вопросов
            heading_id = f"accordion__heading-{i}"
            time.sleep(3)  # Приостанавливает выполнение на 1 секунду
            self.click_arrow(heading_id)


    def click_arrow(self, heading_id):
    # Кликаем по заголовку вопроса с указанным ID
        arrow_selector = heading_id
        arrow = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, arrow_selector)))
        arrow.click()

    def is_text_opened(self, question_number):
    # Ищем элемент с текстом вопроса по его номеру
        question_text_selector = f"accordion__panel-{question_number}"
        try:
        # Ждём, пока элемент станет видимым
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, question_text_selector)))
            return True
        except TimeoutException:
            return False
        
       


    # Локаторы для элементов на главной странице
    
    SCOOTER_LOGO = (By.NAME, "Scooter")
    YANDEX_LOGO = (By.NAME, "Yandex")

    def click_order_button_top(self):
        self.driver.find_element(*self.ORDER_BUTTON_TOP).click()
        return MainPage(self.driver)

    def click_order_button_bottom(self):
        self.driver.find_element(*self.ORDER_BUTTON_BOTTOM).click()
        return MainPage(self.driver)

    def click_scooter_logo_and_check(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Не удалось перейти на главную страницу 'Самоката'"

    def click_yandex_logo_and_check(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()
        assert self.driver.current_url.startswith("https://dzen.ru/"), "Не удалось перейти на главную страницу Дзена"


