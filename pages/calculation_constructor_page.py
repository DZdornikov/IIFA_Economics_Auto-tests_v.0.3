import allure
from pages.base_page import BasePage
from config import current_stand
from locators.calculation_constructor_locators import CalculationConstructorLocators as CCLocators
from files.files_list import CalculationConstructorFilesList as CCFiles
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

    # Функция для удаления всех мастеркниг со стенда
    def delete_all_masterbooks(self):
        if not self.visible_element_present(CCLocators.first_MB):
            # Если на стенде нет МастерКниг, то пропускаем удаление
            pass
        mb_num = 0
        with allure.step("Подчет всех МК на стенде"):
            for i in range(1, 101):
                mb_locator = (By.CSS_SELECTOR,
                              '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div.Mu'
                              'iGrid-root.css-rfnosa > div:nth-child(' + str(i + 1) + ')')
                if not self.visible_element_present(mb_locator):
                    mb_num = i - 1
                    break
        with allure.step("Удаление всех МК на стенде"):
            for k in range(mb_num):
                self.click_on_visible_element(CCLocators.additional_menu_first_MB)
                self.click_on_visible_element(CCLocators.second_button_MB)
                self.click_on_visible_element(CCLocators.confirm_delete_button_MB)
                sleep(1)
        with allure.step("Проверка остались ли МК на странице"):
            if self.visible_element_present(CCLocators.first_MB):
                assert False, "Какая-то из мастеркниг не удалилась со стенда"
        with allure.step("F5 и повторная проверка"):
            self.refresh()
            sleep(1)
            if not self.visible_element_present(CCLocators.first_MB):
                pass
            else:
                assert False, "Какая-то из мастеркниг не удалилась со стенда."

    # Функция, которая считает мастеркниги на стенде и возвращает их количество
    def mb_counter(self):
        mb_num = 0
        for i in range(1, 101):
            mb_locator = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div >'
                                           ' div > div.MuiGrid-root.css-rfnosa > div:nth-child(' + str(i + 1) + ')')
            if not self.visible_element_present(mb_locator):
                break
            mb_num += 1
        return mb_num

    # Функция, которая принимает название МК и список его кейсов. Проходится по всем МК, находит нужную, открывает,
    # считает кейсы, сверяет их число с ожидаемым
    def mb_checker(self, mb_name, mb_list):
        # TODO: ИНТЕГРИРОВАТЬ СТЕПЫ АЛЛЮРА БЕЗ КОСТЫЛЕЙ
        if not self.visible_element_present(CCLocators.first_MB):
            assert False, "МастерКниги отсутствуют на стенде"
        mb_num = self.mb_counter()
        case_counter = 0
        # Проходимся по всем МК
        for i in range(1, mb_num + 1):
            mb_locator = (By.CSS_SELECTOR,
                          '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div.MuiGri'
                          'd-root.css-rfnosa > div:nth-child(' + str(i + 1) + ') > div > div > p')
            # Ищем конкретную МК
            if self.text_of_visible_element(mb_locator) == mb_name:
                # Раскрываем нужную МК
                self.click_on_visible_element((By.CSS_SELECTOR,
                                               '#root > div.MuiBox-root.css-18cq61h > div:nth-child(3) > div > div > di'
                                               'v:nth-child(1) > div > div > div > div.MuiGrid-root.css-rfnosa > div:nt'
                                               'h-child(' + str(i + 1) + ') > div > div:nth-child(2) > svg'))

                if not self.visible_element_present((By.CSS_SELECTOR,
                                                     '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > d'
                                                     'iv > div > div > div> div > div.MuiCollapse-root.MuiCollapse-vert'
                                                     'ical.MuiCollapse-entered.css-c4sutr > div > div > div > div > ul '
                                                     '> div:nth-child(1)')):
                    assert False, "Не найден кейс, похоже, что загрузилась пустая МК"
                # Проходимся по кейсам
                for j in range(1, len(mb_list)):
                    case_locator = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > d'
                                                     'iv > div > div > div> div > div.MuiCollapse-root.MuiCollapse-vert'
                                                     'ical.MuiCollapse-entered.css-c4sutr > div > div > div > div > ul '
                                                     '> div:nth-child(' + str(j + 1) + ') > div > li > span')
                    # Сравниваем название кейса с названием из списка
                    for k in range(len(mb_list)):
                        if self.text_of_visible_element(case_locator) == mb_list[k]:
                            case_counter += 1

                if case_counter != len(mb_list):
                    assert False, "Потерян один из кейсов"
                elif case_counter == len(mb_list):
                    # Закрываем список кейсов
                    self.click_on_visible_element((By.CSS_SELECTOR,
                                                   '#root > div.MuiBox-root.css-18cq61h > div:nth-child(3) > div > div '
                                                   '> div:nth-child(1) > div > div > div > div.MuiGrid-root.css-rfnosa '
                                                   '> div:nth-child(' + str(i + 1) +
                                                   ') > div > div:nth-child(2) > svg'))
                    pass
            else:
                continue

    # Функция, которая принимает название МК и максимальный таймер ожидания. Загружает МК на стенд и запускает проверки
    # по всем консолидациям
    def upload_mb(self, mb_name, timer):
        # Блок, который разбирается какую консолидацию и список кейсов прикрепить в запрос к чекеру
        if mb_name == CCFiles.MB_GEE_filename:
            file, cons_list, cases_list = CCFiles.MB_GEE_dir, CCFiles.MB_GEE_consolidations, CCFiles.MB_GEE_cases
        elif mb_name == CCFiles.MB_KUV_filename:
            file, cons_list, cases_list = CCFiles.MB_KUV_dir, CCFiles.MB_KUV_consolidations, CCFiles.MB_KUV_cases
        elif mb_name == CCFiles.MB_CNT_filename:
            file, cons_list, cases_list = CCFiles.MB_CNT_dir, CCFiles.MB_CNT_consolidations, CCFiles.MB_CNT_cases
        elif mb_name == CCFiles.MB_YUUNG_filename:
            file, cons_list, cases_list = CCFiles.MB_YUUNG_dir, CCFiles.MB_YUUNG_consolidations, CCFiles.MB_YUUNG_cases
        elif mb_name == CCFiles.MB_YUUNG_BUR_filename:
            file, cons_list, cases_list = CCFiles.MB_YUUNG_BUR_dir, CCFiles.MB_YUUNG_BUR_consolidations, \
                                           CCFiles.MB_YUUNG_BUR_cases
        elif mb_name == CCFiles.MB_YAG_filename:
            file, cons_list, cases_list = CCFiles.MB_YAG_dir, CCFiles.MB_YAG_consolidations, CCFiles.MB_YAG_cases
        else:
            assert False, "Неизвестное название МК"

        with allure.step("Подсчет МК на стенде до начала загрузки"):
            mb_num = self.mb_counter()
        with allure.step("Загрузка файла и ожидание его появления на фронте"):
            self.send_keys_to_hidden_element(CCLocators.upload_MB, file)
            for i in range(timer // 6):
                new_mb_num = self.mb_counter()
                if new_mb_num > mb_num:
                    break
        with allure.step("Проверка что при загрузке ничего не потерялось"):
            for j in range(len(cons_list)):
                self.mb_checker(cons_list[j], cases_list[j])
