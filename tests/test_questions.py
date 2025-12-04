from typing import Literal
import allure
import pytest
from config import BASE_URL
from pages.main_page import MainPage
from selenium import webdriver

class TestDropdownList:
    @allure.title("Проверка выпадающего списка вопросов")
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
    def test_dropdown_list(self, driver, question_number: Literal[1] | Literal[2] | Literal[3] | Literal[4] | Literal[5] | Literal[6] | Literal[7] | Literal[8], question_text: Literal['Сколько это стоит? И как оплатить?'] | Literal['Хочу сразу несколько самокатов! Так можно?'] | Literal['Как рассчитывается время аренды?'] | Literal['Можно ли заказать самокат прямо на сегодня?'] | LiteralString | Literal['Вы привозите зарядку вместе с самокатом?'] | Literal['Можно ли отменить заказ?'] | Literal['Я живу за МКАДом, привезёте?']):
        with allure.step("Инициализация драйвера и страницы"):
            page = MainPage(driver)
        
        with allure.step("Открыть страницу"):
            page.open()
        
        with allure.step(f"Нажать на стрелку вопроса №{question_number}"):
            page.click_arrow(question_number)  # метод, который кликает по стрелке вопроса с указанным номером
        
        with allure.step(f"Проверить, что текст для вопроса '{question_text}' открылся"):
            assert page.is_text_opened(question_number), f"Текст для вопроса '{question_text}' не открылся при нажатии на стрелку"


