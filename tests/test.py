import unittest
from pages.base_page import BasePage
from locators.guide_locators import GuideLocators as GL
from time import sleep  # Для ожиданий

# URL страниц отчетов
guide_current_page = "http://genrestest.nntc.pro/economics/guide"


class TestShadowDOM(BasePage):

    def test_dom(self, sign_in_to_stand):
        sleep(10)
        if self.click_on_shadow_element(GL.shadow_guide):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка Справочники не обнаружена"

    sleep(10)


if __name__ == '__main__':
    unittest.main()
