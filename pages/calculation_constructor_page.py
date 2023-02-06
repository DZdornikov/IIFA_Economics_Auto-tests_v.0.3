from pages.base_page import BasePage
from config import current_stand
from locators.calculation_constructor_locators import CalculationConstructorLocators as CCLocators
from selenium.webdriver.common.by import By
from time import sleep

# Переменные
calculation_current_stand = current_stand + "calculation-constructor"


class CalculationConstructorPage(BasePage):

    # Функция для проверки корректная ли страница открыта
    def is_page_calculation_page(self):
        assert self.check_url(calculation_current_stand), \
             "Открыта страница, отличная от Конструктора расчетов"

    # Функция для перехода в Конструктор расчетов
    def move_to_calculation_constructor_page(self):
        assert self.check_url(current_stand), "Открыта страница, отличная от стенда экономики"
        self.click_on_visible_element(CCLocators.move_to_calculation_constructor_page_button)

    def delete_all_masterbooks(self):
        if not self.visible_element_present(CCLocators.first_MB):
            # Если на стенде нет МастерКниг, то пропускаем удаление
            pass
        mb_num = 0
        for i in range(1, 101):
            mb_locator = (By.CSS_SELECTOR,
                          '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div.MuiGri'
                          'd-root.css-rfnosa > div:nth-child(' + str(i + 1) + ')')
            if not self.visible_element_present(mb_locator):
                mb_num = i - 1
                break
        for k in range(mb_num):
            self.click_on_visible_element(CCLocators.additional_menu_first_MB)
            self.click_on_visible_element(CCLocators.second_button_MB)
            self.click_on_visible_element(CCLocators.confirm_delete_button_MB)
            sleep(1)
        self.refresh()
        sleep(1)
        if not self.visible_element_present(CCLocators.first_MB):
            pass
        else:
            assert False, "Какая-то из мастеркниг не удалилась со стенда."

