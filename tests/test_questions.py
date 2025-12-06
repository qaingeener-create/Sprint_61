import pytest
import allure
from config import BASE_URL
from pages.main_page import MainPage
from selenium import webdriver

class TestDropdownList:
    @allure.title("Проверка выпадающего списка вопросов")
    @pytest.mark.parametrize("question_number, question_text", [
        (0, "Сколько это стоит? И как оплатить?"),
        (1, "Хочу сразу несколько самокатов! Так можно?"),
        (2, "Как рассчитывается время аренды?"),
        (3, "Можно ли заказать самокат прямо на сегодня?"),
        (4, "Можно ли продлить заказ или вернуть самокат раньше?"),
        (5, "Вы привозите зарядку вместе с самокатом?"),
        (6, "Можно ли отменить заказ?"),
        (7, "Я жизу за МКАДом, привезёте?")
    ])
    def test_dropdown_list(self, driver, question_number, question_text):
        with allure.step("Инициализация драйвера и страницы"):
            page = MainPage(driver)
        
        with allure.step("Открыть страницу"):
            page.open()
            question_id = f"accordion__heading-{question_number}"
            
        
        with allure.step(f"Нажать на стрелку вопроса №{question_number}"):
            question_id = f"accordion__heading-{question_number}"
            page.click_arrow(question_id)  # метод, который кликает по стрелке вопроса с указанным номером
        
        with allure.step(f"Проверить, что текст для вопроса '{question_text}' открылся"):
            assert page.is_text_opened(question_number), f"Текст для вопроса '{question_text}' не открылся при нажатии на стрелку"
 


