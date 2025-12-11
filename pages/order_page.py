from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from config import BASE_URL
import time

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Используем инициализацию из BasePage

    def open(self):
        self.driver.get(BASE_URL)

    # Локаторы для элементов на главной странице
    ORDER_BUTTON_TOP = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')

    def click_order_button_top(self):
        self.find_element(self.ORDER_BUTTON_TOP).click()  # Используем метод find_element из BasePage
        return OrderPage(self.driver)

    def click_order_button_bottom(self):
        self.find_element(self.ORDER_BUTTON_BOTTOM).click()
        return OrderPage(self.driver)

    # Локаторы для элементов на странице заказа
    input_name = (By.XPATH, "//input[@placeholder='* Имя']")
    input_lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    input_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    input_metro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    select_item_in_dropdown_metro = (By.XPATH, ".//li[@class='select-search__row']")
    input_phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, "//button[text()='Далее']")

    def fill_form(self, name, surname, address, metro_station, phone):
        # Методы для заполнения полей формы заказа
        self.find_element(self.input_name).send_keys(name)
        self.find_element(self.input_lastname).send_keys(surname)
        self.find_element(self.input_address).send_keys(address)
        # Выбор станции метро из выпадающего списка
        metro_input = self.find_element(self.input_metro)
        metro_input.send_keys(metro_station)
        # Предполагаем, что после ввода текста в поле появляются варианты для выбора
        # Выбираем первый предложенный вариант станции метро
        self.wait.until(lambda driver: self.find_element(*self.select_item_in_dropdown_metro)).click()

        self.find_element(self.input_phone).send_keys(phone)

    # Остальные методы...

    def click_next_button(self):
        self.find_element(self.button_next).click()


    def click_next_button(self):
        self.driver.find_element(*self.button_next).click()

        # Экран "Про аренду"
    title_page_rent_info = (By.XPATH, "//div[text()='Про аренду' and contains(@class, 'Order_Header')]")
    input_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    calendar = (By.XPATH, "//div[@class='react-datepicker-popper']")
    calendar_item = (By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")
    field_rental_period = (By.XPATH, ".//div[text()='* Срок аренды']")
    dropdown_item_rental_period = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    checkbox_grey_color_scooter = (By.XPATH, "//input[@id='grey']")
    input_comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    button_make_order = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    def select_delivery_time(self, time):
        # Открываем поле для ввода даты
        self.find_element(self.input_date).click()

        # Находим элемент календаря и выбираем нужную дату
        calendar = self.find_element(self.calendar)
        date_elements = calendar.find_elements(*self.calendar_)

        for date_element in date_elements:
            if date_element.text == time:
                date_element.click()
                break

    def select_rental_period(self, period):
    # Находим элемент для выбора срока аренды
        rental_period_element = self.driver.find_element(*self.field_rental_period)
    
    # Логика выбора периода аренды может различаться в зависимости от реализации интерфейса
    # Например, если это выпадающий список, то можно использовать следующий подход:
        if period == "трое суток":
            self.driver.find_element(*self.dropdown_item_rental_period).click()
        else:
        # Здесь можно добавить логику для других периодов аренды
            pass
    def select_scooter_color(self, color):
        if color == "чёрная жемчуг":
            self.driver.find_element(*self.checkbox_grey_color_scooter).click()
        elif color == "серая безысходность":
        # Здесь должен быть код для выбора другого цвета, например:
            self.driver.find_element(*self.another_color_loc).click()
        else:
            print(f"Цвет {color} не поддерживается.")

    def enter_comment(self, comment):
        self.driver.find_element(*self.input_comment).send_keys(comment)

    def  button_make_order_click(self):  
        self.driver.find_element(*self.button_make_order).click()




    #def is_success_message_present(self):
        # Проверка наличия сообщения об успешном создании заказа
        #return self.wait.until(lambda driver: driver.find_element(*self.SUCCESS_MESSAGE).is_displayed())

    
  