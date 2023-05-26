from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


# TODO: ВЫКИНУТЬ ОТСЮДА ХАРДКОД ТЕНЕВЫХ ЭЛЕМЕНТОВ, ИСПОЛЬЗОВАТЬ НЕПОСРЕДСТВЕННО В ФУНКЦИЯХ ТЕСТА. МЕТОД ДОЛЖЕН ЗАДАВАТЬ
#  СЯ ПЕРЕМЕННОЙ

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def refresh(self):
        self.driver.refresh()

    # Функция, которая проверяет наличие видимого элемента на странице и возвращает его, если он есть
    def visible_element(self, locator):
        try:
            return Wait(self.driver, 5).until((ec.visibility_of_element_located(locator)))
        except TimeoutException:
            raise Exception("Элемент не найден")

    # Функция, которая проверяет наличие скрытого элемента на странице и возвращает его, если он есть
    def hidden_element(self, locator):
        try:
            return Wait(self.driver, 5).until((ec.presence_of_element_located(locator)))
        except TimeoutException:
            raise Exception("Элемент не найден")

    def visible_element_present(self, locator):
        try:
            _ = Wait(self.driver, 5).until((ec.visibility_of_element_located(locator)))
        except TimeoutException:
            return False
        return True

    # Проверяет кликабельный ли элемент и возвращает boolean
    @staticmethod
    def element_is_clickable(locator):
        return ec.element_to_be_clickable(locator)

    # Нужен метод, который будет проверять наличие элемента на странице

    # Возвращает url открытой страницы
    def current_url(self):
        return self.driver.current_url

    # Проверяет соответствие url открытой страницы с url, подаваемым в качестве аргумента. Возвращает boolean
    def check_url(self, url):
        return self.driver.current_url == url

    # Ищет видимый элемент, проверяет кликабельный ли он, если да, то кликает. При ошибке выдает assertion error
    def click_on_visible_element(self, locator):
        try:
            element = Wait(self.driver, 5).until((ec.visibility_of_element_located(locator)))
            if not ec.element_to_be_clickable(element):
                raise Exception("Элемент не кликабельный")
            return element.click()
        except TimeoutException:
            raise Exception("Элемент не найден")

    # Ищет скрытый элемент, проверяет кликабельный ли он, если да, то кликает. При ошибке выдает assertion error
    def click_on_hidden_element(self, locator):
        try:
            element = Wait(self.driver, 5).until((ec.presence_of_element_located(locator)))
            if not ec.element_to_be_clickable(element):
                raise Exception("Элемент не кликабельный")
            return element.click()
        except TimeoutException:
            raise Exception("Элемент не найден")

    def click_on_shadow_element(self, locator):
        try:
            shadow_host = Wait(self.driver, 5).until(
                ec.presence_of_element_located(locator))
            shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
            shadow_element = Wait(shadow_root, 5).until(ec.presence_of_element_located(locator))
            return shadow_element.click()
        except TimeoutException:
            raise Exception("Элемент не найден")

    # Ищет видимый элемент, отправляет в него аргумент. При ошибке выдает assertion error
    def send_keys_to_visible_element(self, locator, keys):
        try:
            element = Wait(self.driver, 5).until((ec.visibility_of_element_located(locator)))
            return element.send_keys(keys)
        except TimeoutException:
            raise Exception("Элемент не найден")

    # Ищет скрытый элемент, отправляет в него аргумент. При ошибке выдает assertion error
    def send_keys_to_hidden_element(self, locator, keys):
        try:
            element = Wait(self.driver, 5).until((ec.presence_of_element_located(locator)))
            return element.send_keys(keys)
        except TimeoutException:
            raise Exception("Элемент не найден")

    def send_keys_to_shadow_element_wifi_login(self, locator, keys):
        try:
            shadow_host = Wait(self.driver, 5).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/form/div[1]/div/div/input')))
            shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
            shadow_element = Wait(shadow_root, 5).until(ec.presence_of_element_located(locator))
            return shadow_element.send_keys(keys)
        except TimeoutException:
            raise Exception("Элемент не найден")

    def send_keys_to_shadow_element_wifi_password(self, locator, keys):
        try:
            shadow_host = Wait(self.driver, 5).until(
                ec.presence_of_element_located((By.XPATH, '// *[ @ id = "app"] / div / div / form / div[2] / div / div '
                                                          '/ input')))
            shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
            shadow_element = Wait(shadow_root, 5).until(ec.presence_of_element_located(locator))
            return shadow_element.send_keys(keys)
        except TimeoutException:
            raise Exception("Элемент не найден")

    # Ищет видимый элемент, возвращает его текст. При ошибке выдает assertion error
    def text_of_visible_element(self, locator):
        try:
            element = Wait(self.driver, 5).until((ec.visibility_of_element_located(locator)))
            return element.text
        except TimeoutException:
            raise Exception("Элемент не найден")

    # Ищет скрытый элемент, возвращает его текст. При ошибке выдает assertion error
    def text_of_hidden_element(self, locator):
        try:
            element = Wait(self.driver, 5).until((ec.presence_of_element_located(locator)))
            return element.text
        except TimeoutException:
            raise Exception("Элемент не найден")

    # Ищет видимый элемент, возвращает его аттрибут. При ошибке выдает assertion error
    def attribute_of_visible_element(self, locator, attribute):
        try:
            element = Wait(self.driver, 5).until((ec.visibility_of_element_located(locator)))
            return element.get_attribute(attribute)
        except TimeoutException:
            raise Exception("Элемент не найден")

    # Ищет скрытый элемент, возвращает его аттрибут. При ошибке выдает assertion error
    def attribute_of_hidden_element(self, locator, attribute):
        try:
            element = Wait(self.driver, 5).until((ec.presence_of_element_located(locator)))
            return element.get_attribute(attribute)
        except TimeoutException:
            raise Exception("Элемент не найден")
