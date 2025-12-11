import allure
import pytest
from config import BASE_URL
from pages.order_page import OrderPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import order_data
    


class TestOrderFlow:
    @allure.title("Тестирование потока заказа через верхнюю кнопку")
    @pytest.mark.parametrize("order_data", order_data)
    def test_order_flow(self,driver,order_data):

    
        page = OrderPage(driver)
        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Нажать на кнопку 'Заказать' вверху страницы"):
            order_page_top = page.click_order_button_top()
        
        with allure.step("Заполнить форму заказа"):
            order_page_top.fill_form(order_data["name"], order_data["surname"], order_data["address"], order_data["metro_station"], order_data["phone"])
        
        with allure.step("Нажать кнопку 'Далее'"):
            order_page_top.click_next_button()
        
        with allure.step("Заполнить дополнительные поля"):
            order_page_top.select_delivery_time("Когда привезти самокат")
            order_page_top.select_rental_period("Срок аренды")
            order_page_top.select_scooter_color("чёрная жемчуг")  # или "серая безысходность"
            order_page_top.enter_comment("Комментарий для курьера")
        
        assert order_page_top.is_success_message_present(), "Сообщение об успешном создании заказа не появилось"

    @allure.title("Тестирование потока заказа через нижнюю кнопку")
    @pytest.mark.parametrize("order_data", [
        {
            "name": "Иван",
            "surname": "Иванов",
            "address": "ул. Примерная, д. 1",
            "metro_station": "Щёлковская",
            "phone": "89046777833"
        },
        {
            "name": "Мария",
            "surname": "Петрова",
            "address": "пр-т Ленинский, д. 2",
            "metro_station": "ВДНХ",
            "phone": "89876543214"
        }
    ])
    def test_order_flow_bottom_button(self, driver, order_data: dict[str, str]):
        page = OrderPage(driver)
        with allure.step("Открыть главную страницу"):
            page.open()
        with allure.step("Прокрутить страницу вниз"):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    
            

        with allure.step("Нажать на кнопку 'Заказать' внизу страницы"):
            order_page_bottom = page.click_order_button_bottom()
        
        with allure.step("Заполнить форму заказа"):
            order_page_bottom.fill_form(order_data["name"], order_data["surname"], order_data["address"], order_data["metro_station"], order_data["phone"])
        
        with allure.step("Нажать кнопку 'Далее'"):
            order_page_bottom.click_next_button()
        
        with allure.step("Заполнить дополнительные поля"):
            order_page_bottom.select_delivery_time("Когда привезти самокат")
            order_page_bottom.select_rental_period("Срок аренды")
            order_page_bottom.select_scooter_color("чёрная жемчуг")  # или "серая безысходность"
            order_page_bottom.enter_comment("Комментарий для курьера")
        with allure.step("Проверить отображение дополнительных полей"):
            assert order_page_bottom.are_additional_fields_present(), "Дополнительные поля не отображаются"

        

    @allure.title("Тестирование ссылки на логотип 'Самоката'")
    def test_scooter_logo_link(self, driver,):
        page = OrderPage(driver)
        with allure.step("Открыть главную страницу"):
            page.open()
        with allure.step("Нажать на логотип 'Самоката'"):
            page.click_scooter_logo()
        with allure.step("Проверить перенаправление на страницу 'Самоката'"):
            assert page.is_scooter_page_opened(), "Перенаправление на страницу 'Самоката' не произошло"

    @allure.title("Тестирование ссылки на лого 'Яндекса'")
    def test_yandex_logo_link(self, driver):
        page = OrderPage(driver)
        with allure.step("Открыть главную страницу"):
            page.open()
        with allure.step("Нажать на лого 'Яндекса'"):
            page.click_yandex_logo()
        with allure.step("Проверить перенаправление на страницу 'Яндекса'"):
            assert page.is_yandex_page_opened(), "Перенаправление на страницу 'Яндекса' не произошло"


        

