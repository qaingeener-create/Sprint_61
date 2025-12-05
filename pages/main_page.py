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
        self.scroll_into_view()  # Прокручиваем страницу сразу после открытия

    def scroll_into_view(self):
    #Прокручивает страницу так, чтобы нужный элемент стал видимым.
        element = self.driver.find_element(By.CLASS_NAME, "accordion")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_arrow(self, heading_id):
    # Кликаем по заголовку вопроса с указанным ID
        arrow_selector = f"#{heading_id}"
        arrow = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, arrow_selector)))
        arrow.click()


    
   
    def open_all_questions(self):
        for i in range(8):  # Предполагаем, что у нас есть 8 вопросов
            heading_id = f"accordion__heading-{i}"
            self.click_arrow(heading_id)
        # Здесь можно добавить небольшую задержку, если необходимо
        # time.sleep(1)

    
    

    # Локаторы для элементов на главной странице
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, ".button.Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_UltraBig__UU3Lp")
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


