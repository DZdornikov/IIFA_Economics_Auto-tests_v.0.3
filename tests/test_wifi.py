import pytest
from pages.wifi_page import WifiPage as WP
from time import sleep
from pages.base_page import BasePage as BP              # Для рефреша страницы
import keyboard

class TestWifi:

    def test_wifi(self, sign_in_to_stand):
