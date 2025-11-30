from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.main_page import MainPage

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы для элементов на странице заказа
    NAME_FIELD = (By.ID, "name")
    SURNAME_FIELD = (By.ID, "surname")
    ADDRESS_FIELD = (By.ID, "address")
    METRO_STATION_SELECT = (By.ID, "metro-station")
    PHONE_FIELD = (By.ID, "phone")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")

    def fill_form(self, name, surname, address, metro_station, phone):
        # Методы для заполнения полей формы заказа
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)
        self.driver.find_element(*self.SURNAME_FIELD).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)
        # Выбор станции метро из выпадающего списка
        pass
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)

    def is_success_message_present(self):
        # Проверка наличия сообщения об успешном создании заказа
        return self.wait.until(lambda driver: driver.find_element(*self.SUCCESS_MESSAGE).is_displayed())