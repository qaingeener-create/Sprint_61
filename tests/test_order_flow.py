import pytest

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
def test_order_flow(order_data):
    main_page = MainPage()  # предположим, что у вас есть класс MainPage
    main_page.open()

    # Тестирование первой точки входа - кнопка "Заказать" вверху страницы
    order_page_top = main_page.click_order_button_top()  # метод для клика по кнопке "Заказать" вверху
    order_page_top.fill_form(order_data["name"], order_data["surname"], order_data["address"], order_data["metro_station"], order_data["phone"])  # метод для заполнения формы заказа
    assert order_page_top.is_success_message_present(), "Сообщение об успешном создании заказа не появилось"

    # Повторное открытие главной страницы для новой попытки
    main_page.open()

    # Тестирование второй точки входа - кнопка "Заказать" внизу страницы
    order_page_bottom = main_page.click_order_button_bottom()  # метод для клика по кнопке "Заказать" внизу
    order_page_bottom.fill_form(order_data["name"], order_data["surname"], order_data["address"], order_data["metro_station"], order_data["phone"])  # метод для заполнения формы заказа
    assert order_page_bottom.is_success_message_present(), "Сообщение об успешном создании заказа не появилось"

    # Проверка перехода по лого "Самоката"
    main_page = MainPage()
    main_page.open()
    assert main_page.click_scooter_logo_and_check(), "Не удалось перейти на главную страницу 'Самоката'"

    # Проверка перехода по лого Яндекса
    main_page = MainPage()
    main_page.open()
    assert main_page.click_yandex_logo_and_check(), "Не удалось перейти на главную страницу Дзена"