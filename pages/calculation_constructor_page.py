import os

import allure
from pages.base_page import BasePage
from config import current_stand, downloads_dir
from locators.calculation_constructor_locators import CalculationConstructorLocators as CCLocators
from locators.report_locators import ReportLocators as RLocators
from files.files_list import CalculationConstructorFilesList as CCFiles
from selenium.webdriver.common.by import By
from os import path
from time import sleep
from random import randint

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
            return
        with allure.step("Подчет всех МК на стенде"):
            mb_num = CalculationConstructorPage.mb_counter(self)
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
        for i in range(1, 1001):
            mb_locator = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div >'
                                           ' div > div.MuiGrid-root.css-rfnosa > div:nth-child(' + str(i + 1) + ')')
            if not self.visible_element_present(mb_locator):
                break
            mb_num += 1
        return mb_num

    # Функция считает ФЭМ на стенде и возвращает их количество
    def fem_counter(self):
        fem_num = 0
        self.click_on_visible_element(CCLocators.open_FEM_menu_button)
        for i in range(1, 101):
            fem_loc = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div > div > di'
                                        'v > div > div.MuiCollapse-root.MuiCollapse-vertical.MuiCollapse-entered.css-c4'
                                        'sutr > div > div > div > div > ul > li:nth-child(' + str(i) + ')')
            if self.visible_element_present(fem_loc):
                fem_num += 1
            else:
                break
        self.click_on_visible_element(CCLocators.open_FEM_menu_button)
        return fem_num

    # Функция считает макропараметры на стенде и возвращает их количество
    def macro_counter(self):
        macro_num = 0
        self.click_on_visible_element(CCLocators.open_Macro_menu_button)
        for i in range(1, 101):
            macro_loc = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div > div > '
                                          'div > div > div.MuiCollapse-root.MuiCollapse-vertical.MuiCollapse-entered.cs'
                                          's-c4sutr > div > div > div > div > ul > li:nth-child(' + str(i) + ')')
            if self.visible_element_present(macro_loc):
                macro_num += 1
            else:
                break
        self.click_on_visible_element(CCLocators.open_Macro_menu_button)
        return macro_num

    # Функция, которая принимает название МК и список его кейсов. Проходится по всем МК, находит нужную, открывает,
    # считает кейсы, сверяет их число с ожидаемым
    def mb_checker(self, mb_name, mb_list):
        if not self.visible_element_present(CCLocators.first_MB):
            assert False, "МастерКниги отсутствуют на стенде"
        mb_num = CalculationConstructorPage.mb_counter(self)
        case_counter = 0
        # Проходимся по всем МК
        for i in range(1, mb_num + 1):
            mb_locator = (By.CSS_SELECTOR,
                          '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div.MuiGri'
                          'd-root.css-rfnosa > div:nth-child(' + str(i + 1) + ') > div > div > p')
            if self.text_of_visible_element(mb_locator) == mb_name:
                mb_opener_locator = (By.CSS_SELECTOR,
                                     '#root > div.MuiBox-root.css-18cq61h > div:nth-child(3) > div > div > div:nth-chil'
                                     'd(1) > div > div > div > div.MuiGrid-root.css-rfnosa > div:nth-child(' +
                                     str(i + 1) + ') > div > div:nth-child(2) > svg')
                self.click_on_visible_element(mb_opener_locator)
                if not self.visible_element_present((By.CSS_SELECTOR,
                                                     '#root > div > div:nth-child(3) > div > di'
                                                     'v > div:nth-child(1) > div > div > div > div.MuiGrid-root.css-rfn'
                                                     'osa > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPa'
                                                     'per-elevation1.MuiAccordion-root.MuiAccordion-rounded.Mui-expande'
                                                     'd.MuiAccordion-gutters.css-1wsq4x7 > div.MuiCollapse-root.MuiColl'
                                                     'apse-vertical.MuiCollapse-entered.css-c4sutr > div > div > div > '
                                                     'div > ul > div:nth-child(1) > div > li > span')):
                    assert False, "Не найден кейс, похоже, что загрузилась пустая МК"
                for j in range(1, len(mb_list)+1):
                    for k in range(len(mb_list)):
                        case_locator = (By.CSS_SELECTOR,
                                        '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div > di'
                                        'v > div> div > div.MuiCollapse-root.MuiCollapse-vertical.MuiCollapse-entered.c'
                                        'ss-c4sutr > div > div > div > div > ul > div:nth-child(' + str(j) +
                                        ') > div > li > span')
                        case_name = self.text_of_visible_element(case_locator)
                        if case_name == mb_list[k]:
                            case_counter += 1
                            break
                if case_counter != len(mb_list):
                    assert False, "Потерян один из кейсов"
                elif case_counter == len(mb_list):
                    # Закрываем список кейсов
                    self.click_on_visible_element(mb_opener_locator)
                    pass
                else:
                    continue

    # Функция, которая принимает название МК и максимальный таймер ожидания. Загружает МК на стенд и запускает проверки
    # по всем консолидациям
    def upload_mb(self, mb_name, timer=300, check=True):
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

        mb_num = CalculationConstructorPage.mb_counter(self)
        self.send_keys_to_hidden_element(CCLocators.upload_MB, file)
        for i in range(timer // 6):
            new_mb_num = CalculationConstructorPage.mb_counter(self)
            if new_mb_num > mb_num:
                break
        if check:
            for j in range(len(cons_list)):
                CalculationConstructorPage.mb_checker(self, cons_list[j], cases_list[j])

    # Функция выбирает случайный кейс, первые попавшиеся ФЭМ и Макру, производит расчет, скачивает полученный отчет и
    # проверяет скачался ли файл
    def calculate_random_case(self):
        # Подсчет МК на стенде и проверка, если МК на стенде нет, то загрузка
        mb_num = CalculationConstructorPage.mb_counter(self)
        if mb_num == 0:
            # На стенде отсутствуют МК, загружаем рандомную
            mb_list = [CCFiles.MB_GEE_filename, CCFiles.MB_YUUNG_filename, CCFiles.MB_YAG_filename,
                       CCFiles.MB_CNT_filename, CCFiles.MB_KUV_filename, CCFiles.MB_YUUNG_BUR_filename]
            CalculationConstructorPage.upload_mb(self, mb_list[randint(0, len(mb_list)+1)])
        # Подсчет консолидаций
        cons_num = CalculationConstructorPage.mb_counter(self)
        # выбор случайной консолидации и кейса
        if cons_num == 1:
            chosen_cons_num = 2
        else:
            chosen_cons_num = randint(1, cons_num+1)
        chosen_cons_loc = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div '
                                            '> div > div.MuiGrid-root.css-rfnosa > div:nth-child(' +
                           str(chosen_cons_num) + ')')
        self.click_on_visible_element(chosen_cons_loc)
        cases_num = 0
        for i in range(1, 33):
            case_loc = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div > d'
                                         'iv > div> div > div.MuiCollapse-root.MuiCollapse-vertical.MuiCollapse-entered'
                                         '.css-c4sutr > div > div > div > div > ul > div:nth-child(' + str(i) +
                                         ') > div > li > span')
            if self.visible_element_present(case_loc):
                cases_num += 1
            else:
                break
        chosen_case_loc = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div '
                                            '> div > div> div > div.MuiCollapse-root.MuiCollapse-vertical.MuiCollapse-e'
                                            'ntered.css-c4sutr > div > div > div > div > ul > div:nth-child(' +
                           str(randint(1, cases_num)) + ') > div > li > span')
        chosen_case_name = self.text_of_visible_element(chosen_case_loc)
        self.click_on_visible_element(chosen_case_loc)
        # Выбрать первую ФЭМ и первую макру
        # Блок проверки на наличие ФЭМ на фронте
        if CalculationConstructorPage.fem_counter(self) == 0:
            CalculationConstructorPage.upload_fem(self, CCFiles.FEM_NDD_dir)
        self.click_on_visible_element(CCLocators.open_FEM_menu_button)
        self.click_on_visible_element(CCLocators.first_FEM)
        self.click_on_visible_element(CCLocators.open_FEM_menu_button)

        # Блок проверки на наличие макры на фронте
        if CalculationConstructorPage.macro_counter(self) == 0:
            CalculationConstructorPage.upload_macro(self, CCFiles.macro_dir)
        self.click_on_visible_element(CCLocators.open_Macro_menu_button)
        self.click_on_visible_element(CCLocators.first_Macro)
        self.click_on_visible_element(CCLocators.start_calculation_button)

        # Прокликиваем уведомления
        while self.visible_element_present(CCLocators.first_notification):
            self.click_on_visible_element(CCLocators.first_notification)
            sleep(0.25)
        # Проверяем корректно ли открылась страница отчетов
        assert self.check_url(current_stand + "reports"), "Ошибка, открыта страница, отличная от страницы отчетов"
        # Проверям совпадение названия отчета с названием кейса, выбранного ранее
        assert self.text_of_visible_element(RLocators.first_report_name) == chosen_case_name, \
            f"Название сгенерированного отчета не совпадает с названием выбранного кейса. Found - " \
            f"{self.text_of_visible_element(RLocators.first_report_name)}, expected - {chosen_case_name}"
        # Проверяем есть ли документ в папке загрузок с таким именем
        if not path.isfile(downloads_dir + fr"\{chosen_case_name}.xlsx"):
            # Документа нет, проверяем
            self.click_on_visible_element(RLocators.export_report_button)
            sleep(2)
            assert path.isfile(downloads_dir + fr"\{chosen_case_name}.xlsx"), "Файл не найден в папке загрузок после " \
                                                                              "экспорта"
            os.remove(downloads_dir + fr"\{chosen_case_name}.xlsx")
            sleep(1)
            assert not path.isfile(downloads_dir + fr"\{chosen_case_name}.xlsx"), "Файл найден в папке загрузок " \
                                                                                  "после удаления"
        else:
            os.remove(downloads_dir + fr"\{chosen_case_name}.xlsx")
            assert not path.isfile(downloads_dir + fr"\{chosen_case_name}.xlsx"), "Ошибка при удалении файла - файл " \
                                                                                  "не найден"
            self.click_on_visible_element(RLocators.export_report_button)
            sleep(2)
            assert path.isfile(downloads_dir + fr"\{chosen_case_name}.xlsx"), "Файл не найден в папке загрузок после " \
                                                                              "экспорта"
            os.remove(downloads_dir + fr"\{chosen_case_name}.xlsx")
            sleep(1)
            assert not path.isfile(downloads_dir + fr"\{chosen_case_name}.xlsx"), "Файл найден в папке загрузок " \
                                                                                  "после удаления"
        self.click_on_visible_element(CCLocators.move_to_calculation_constructor_page_button)
        sleep(1)
        assert self.check_url(calculation_current_stand), "Ошибка при возврате на страницу конструктора расчетов"

    # Функция удаляет все ФЭМ на стенде
    def delete_all_fem(self):
        fem_num = CalculationConstructorPage.fem_counter(self)
        if fem_num == 0:
            pass
        self.click_on_visible_element(CCLocators.open_FEM_menu_button)
        for i in range(fem_num, 0, -1):
            self.click_on_visible_element(CCLocators.additional_menu_first_FEM)
            sleep(0.5)
            self.click_on_visible_element((By.XPATH, '/html/body/div[' + str(i+1) + ']/div[3]/ul/li/div/span'))
            sleep(0.5)
        self.refresh()
        self.click_on_visible_element(CCLocators.open_FEM_menu_button)
        assert not self.visible_element_present((By.CSS_SELECTOR,
                                                 '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div >'
                                                 ' div > div > div > div.MuiCollapse-root.MuiCollapse-vertical.MuiColla'
                                                 'pse-entered.css-c4sutr > div > div > div > div > ul > li:nth-child(1)'
                                                 )), "ФЭМ найдены после удаления, следовательно удаление не работает"
        self.click_on_visible_element(CCLocators.open_FEM_menu_button)

    # Функция загружает ФЭМ на стенд
    def upload_fem(self, fem_file):
        fem_num = CalculationConstructorPage.fem_counter(self)
        self.click_on_visible_element(CCLocators.open_FEM_menu_button)
        self.send_keys_to_hidden_element(CCLocators.upload_FEM, fem_file)
        self.click_on_visible_element(CCLocators.open_FEM_menu_button)
        new_fem_num = CalculationConstructorPage.fem_counter(self)
        assert (new_fem_num - fem_num) == 1, f"Количество ФЭМ на стенде не совпадает с ожидаемым. Ожидаемое = " \
                                             f"{fem_num + 1}. Фактическое = {new_fem_num}"

    # Функция удаляет все макропараметры для стенда
    def delete_all_macro(self):
        macro_num = CalculationConstructorPage.macro_counter(self)
        if macro_num == 0:
            pass
        self.click_on_visible_element(CCLocators.open_Macro_menu_button)
        for i in range(macro_num, 0, -1):
            self.click_on_visible_element(CCLocators.additional_menu_first_Macro)
            sleep(0.5)
            self.click_on_visible_element((By.XPATH, '/html/body/div[' + str(i+1) + ']/div[3]/ul/li/div/span'))
        self.refresh()
        self.click_on_visible_element(CCLocators.open_Macro_menu_button)
        assert not self.visible_element_present(CCLocators.first_Macro), "Макропараметры найдены после удаления, " \
                                                                         "следовательно удаление не работает"
        self.click_on_visible_element(CCLocators.open_Macro_menu_button)

    # Функция загружает макропараметры на стенд
    def upload_macro(self, macro_file):
        macro_num = CalculationConstructorPage.macro_counter(self)
        self.click_on_visible_element(CCLocators.open_Macro_menu_button)
        self.send_keys_to_hidden_element(CCLocators.upload_Macro, macro_file)
        self.click_on_visible_element(CCLocators.open_Macro_menu_button)
        new_macro_num = CalculationConstructorPage.macro_counter(self)
        assert (new_macro_num - macro_num) == 1, f"Количество ФЭМ на стенде не совпадает с ожидаемым. Ожидаемое = " \
                                                 f"{macro_num + 1}. Фактическое = {new_macro_num}"

    # Функция проверяет наличие элементов в условиях расчета. Проверка осуществляется методом проверки присутствия
    # элементов self.click_on_visible_element() и методом проверки кликабельности self.element_is_clickable()
    def check_calculation_conditions_elements(self):
        element_list = [
            CCLocators.conditions_project_start_input, CCLocators.conditions_project_start_button,
            CCLocators.conditions_infl_start_date_input, CCLocators.conditions_infl_start_date_button,
            CCLocators.conditions_disc_start_input, CCLocators.conditions_disc_start_button,
            CCLocators.conditions_econom_limit_date_input, CCLocators.conditions_econom_limit_date_button,
            CCLocators.conditions_calculation_horizon_input, CCLocators.conditions_date_type_econom_limit_div
        ]
        element_description_list = [
            'input "Начало проекта"', 'кнопка с календариком "Начало проекта"',
            'input "Дата начала инфлирования"', 'кнопка с календариком "Дата начала инфлирования"',
            'input "Начало дисконтирования"', 'кнопка с календариком "Начало дисконтирования"',
            'input "Начало дисконтирования"', 'кнопка с календариком "Дата эконом. предела"',
            'input "Горизонт расчета"', 'список "Тип даты эконом. предела"'
        ]
        self.click_on_visible_element(CCLocators.open_calculation_conditions_menu_button)
        # Блок базовых проверок
        for i in range(len(element_list)):
            assert self.visible_element_present(element_list[i]), f"Отсутствует, либо не видим элемент -> " \
                                                                  f"{element_description_list[i]}"
            assert self.element_is_clickable(element_list[i]), f"Некликабельный элемент -> {element_description_list[i]}"

        # TODO: Сделать подробную проверку полей расчета, как только завезут функционал
        self.click_on_visible_element(CCLocators.open_calculation_conditions_menu_button)

