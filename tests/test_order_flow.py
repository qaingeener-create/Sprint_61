import allure
import pytest
from main_page import MainPage
from selenium import webdriver

from selenium import webdriver

@pytest.mark.parametrize("order_data", [
    {
        "name": "Иван",
        "surname": "Иванов",
        "address": "ул. Примерная, д. 1",
        "metro_station": "Щёлковская",
        "phone": "1234567890"
    },
    {
        "name": "Мария",
        "surname": "Петрова",
        "address": "пр-т Ленинский, д. 2",
        "metro_station": "ВДНХ",
        "phone": "0987654321"
    }
])
def test_order_flow(order_data: dict[str, str]):
    driver = webdriver.Chrome()  # или другой браузер, который вы используете
    page = MainPage(driver) 
    page.open("https://qa-scooter.praktikum-services.ru/")


    # Тестирование первой точки входа - кнопка "Заказать" вверху страницы
    order_page_top = page.click_order_button_top()  # метод для клика по кнопке "Заказать" вверху
    order_page_top.fill_form(order_data["name"], order_data["surname"], order_data["address"], order_data["metro_station"], order_data["phone"])  # метод для заполнения формы заказа
    assert order_page_top.is_success_message_present(), "Сообщение об успешном создании заказа не появилось"

    # Повторное открытие главной страницы для новой попытки
    page.open("https://qa-scooter.praktikum-services.ru/")


    # Тестирование второй точки входа - кнопка "Заказать" внизу страницы
    order_page_bottom = page.click_order_button_bottom()  # метод для клика по кнопке "Заказать" внизу
    order_page_bottom.fill_form(order_data["name"], order_data["surname"], order_data["address"], order_data["metro_station"], order_data["phone"])  # метод для заполнения формы заказа
    assert order_page_bottom.is_success_message_present(), "Сообщение об успешном создании заказа не появилось"

    # Проверка перехода по лого "Самоката"
    page = MainPage()
    page.open("https://qa-scooter.praktikum-services.ru/")

    assert page.click_scooter_logo_and_check(), "Не удалось перейти на главную страницу 'Самоката'"

    # Проверка перехода по лого Яндекса
    page = MainPage()
    page.open("https://qa-scooter.praktikum-services.ru/")

    assert page.click_yandex_logo_and_check(), "Не удалось перейти на главную страницу Дзена"