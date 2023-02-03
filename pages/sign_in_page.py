from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import current_stand
from time import sleep


class SignInPage(BasePage):
    # ЛОКАТОРЫ
    USERNAME = (By.CSS_SELECTOR, '#username')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '#kc-login')

    # МЕТОДЫ

    # Функция для прохождения авторизации. Сама проверяет, корректно ли отработала
    def keycloak_authorization(self):
        username, password = 'dev', 'qwe123R!'
        self.send_keys_to_visible_element(self.USERNAME, username)
        self.send_keys_to_visible_element(self.PASSWORD, password)
        self.click_on_visible_element(self.SIGN_IN_BUTTON)
        sleep(1)
        assert self.check_url(current_stand), "Ошибка, открыта страница, отличная от модуля Экономика"
