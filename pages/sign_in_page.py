from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import current_stand
from time import sleep


class SignInPage(BasePage):
    # ЛОКАТОРЫ
    USERNAME = (By.CSS_SELECTOR, '#username')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '#kc-login')

    USERNAME_WIFI = (By.XPATH, "//*[@id='app']/div/div/form/div[1]/div/div/input")
    PASSWORD_WIFI = (By.XPATH, "//*[@id='app']/div/div/form/div[2]/div/div/input")
    SIGN_IN_BUTTON_WIFI = (By.XPATH, "//*[@id='app']/div/div/button")

    # МЕТОДЫ

    # Функция для прохождения авторизации. Сама проверяет, корректно ли отработала
    def keycloak_authorization(self):
        username, password = 'dev', 'qwe123R!'
        self.send_keys_to_visible_element(self.USERNAME, username)
        self.send_keys_to_visible_element(self.PASSWORD, password)
        self.click_on_visible_element(self.SIGN_IN_BUTTON)
        sleep(1)
        assert self.check_url(current_stand), "Ошибка, открыта страница, отличная от модуля Экономика"

    def wifi_authorization(self):
        username, password = 'Admin', 'Gfhjkm512!'
        self.send_keys_to_visible_element(self.USERNAME_WIFI, username)
        self.send_keys_to_visible_element(self.PASSWORD_WIFI, password)
        self.click_on_visible_element(self.SIGN_IN_BUTTON_WIFI)
        sleep(1)
