import allure
import pytest
from pages.wifi_page import WifiPage as wifi
from time import sleep
import keyboard                                         # Для функционирования с выпадающими окнами без селекторов


class TestWifiPage:
    @allure.feature("Проверка загрузки справочника")
    @allure.story("Чистит стенд, создаёт справочник, его шапку, а затем загружает excel, сверяя с захардкоженными данны"
                  "ми, после чего сохраняет результат")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.guide
    def test_restart_all_wifi_devices(self, sign_in_to_stand):
        sign_in = sign_in_to_stand
        sleep(10)
        wifi.go_to_page(sign_in)
        sleep(10)
        wifi.move_to_wifi_page(sign_in)
        wifi.click_on_devices(sign_in)
        wifi.click_on_list_button(sign_in)
        wifi.click_on_restart_buttons(sign_in)
    sleep(10)

#//*[@id="details-button"]
#//*[@id="proceed-link"]