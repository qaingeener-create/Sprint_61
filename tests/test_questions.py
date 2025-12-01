import allure
import pytest
from config import BASE_URL
from pages.main_page import MainPage
from selenium import webdriver





@pytest.mark.parametrize("question_number, question_text", [
    (1, "Сколько это стоит? И как оплатить?"),
    (2, "Хочу сразу несколько самокатов! Так можно?"),
    (3, "Как рассчитывается время аренды?"),
    (4, "Можно ли заказать самокат прямо на сегодня?"),
    (5, "Можно ли продлить заказ или вернуть самокат раньше?"),
    (6, "Вы привозите зарядку вместе с самокатом?"),
    (7, "Можно ли отменить заказ?"),
    (8, "Я живу за МКАДом, привезёте?")
])
def test_dropdown_list(question_number, question_text):
    driver = webdriver.Chrome()
  
    page = MainPage(driver)
    # остальной код теста
  
    page.open()
    page.click_arrow(question_number)  # метод, который кликает по стрелке вопроса с указанным номером
    assert page.is_text_opened(question_number), f"Текст для вопроса '{question_text}' не открылся при нажатии на стрелку"