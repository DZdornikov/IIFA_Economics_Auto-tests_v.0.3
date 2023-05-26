from time import sleep  # Для ожиданий

from selenium.webdriver.common.by import By

from locators.wifi_locators import WifiLocators as WL
from pages.base_page import BasePage  # Для использования адаптированных функций Selenium

wifi_current_page = "https://100.111.0.25:8070/#/page/index"


class WifiPage(BasePage):

    def move_to_wifi_page(self):
        assert self.check_url(wifi_current_page), \
            "Открыта страница, отличная от Контроллера"

    def click_on_devices(self):
        if self.click_on_visible_element(WL.click_on_devices):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка Девайсов не обнаружена"

    def click_on_list_button(self):
        if self.click_on_visible_element(WL.click_on_list_button):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка Сортировка в листе не обнаружена"

    def click_on_restart_buttons(self):
        for i in range(20):
            self.click_on_visible_element(
                (By.XPATH, "//*[@id='scroll-view']/div[2]/div[2]/div[1]/div[3]/table/tbody/"
                           "tr[' + str(i + 1) + ']/td[8]/div/button[2]"))
            sleep(1)
            pass
        else:
            assert False, "Кнопки перезагрузки Wi-Fi не найдены"

    def go_to_page(self):
        self.driver.get("https://100.111.0.25:8070/#/page/index")
