from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import current_stand


class SignInPage(BasePage):
    # ЛОКАТОРЫ
    USERNAME = (By.CSS_SELECTOR, '#username')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '#kc-login')

    # МЕТОДЫ

    # Функция для прохождения авторизации. Сама проверяет, корректно ли отработала
    def keycloak_authorization(self):
        username = 'dev'
        password = 'qwe123R!'
        pass


