from pages.base_page import BasePage  # Для использования адаптированных функций Selenium
from locators.guide_locators import GuideLocators as GL
from time import sleep  # Для ожиданий
from selenium.webdriver.common.by import By
from config import current_stand

# URL страниц отчетов
guide_current_page = current_stand + 'guide'


class GuidePage(BasePage):

    # Функция для проверки корректная ли страница открыта
    def is_page_guide_page(self):
        assert self.check_url(guide_current_page), \
            "Открыта страница, отличная от Справочников"

    def move_to_guide_page(self):
        assert self.check_url(current_stand), "Открыта страница, отличная от стенда экономики"
        self.click_on_visible_element(GL.move_to_guide_page)

    def create_guide_group(self):
        if self.click_on_visible_element(GL.create_guide_group):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка создания группы справочников не найдена"

    def guide_group_name_print(self):
        if self.click_on_visible_element(GL.guide_name_print):
            sleep(0.5)
            self.send_keys_to_visible_element(GL.guide_name_print, '20012026')
            pass
        else:
            assert False, "Окно ввода названия группы справочников не найдено"

    def guide_group_or_guide_add_button(self):
        if self.click_on_visible_element(GL.guide_group_add_button):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка добавить группу справочников не найдена"

    def open_menu(self):
        if self.click_on_visible_element(GL.open_menu):
            sleep(0.5)
            pass
        else:
            assert False, "Меню группы справочников не открыто"

    def add_guide(self):
        if self.click_on_visible_element(GL.add_guide_button):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка создания справочника не найдена"

    def delete_guide_group(self):
        if self.click_on_visible_element(GL.delete_guide_group):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка удаления не найдена"

    def type_column_number(self):
        if self.click_on_visible_element(GL.type_column_number):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка типа колонки Число не найдена"

    def column_name(self, key_name):
        if self.click_on_visible_element(GL.column_name):
            sleep(0.5)
            self.send_keys_to_visible_element(GL.column_attribute_o_or_p_choose, key_name)
            sleep(0.5)
            pass
        else:
            assert False, "Окно ввода имени колонки не обнаружено"

    def column_dimension(self):
        if self.click_on_visible_element(GL.column_dimension):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка размерности колонки не обнаружена"

    def column_purpose(self):
        if self.click_on_visible_element(GL.column_purpose):
            sleep(0.5)
            pass
        else:
            assert False, "Окно выбора назначения не обнаружено"

    def search_guide_window(self):
        if self.click_on_visible_element(GL.search_guide_window):
            sleep(0.5)
            self.send_keys_to_visible_element(GL.search_guide_window, '20012026')
            sleep(0.5)
            pass
        else:
            assert False, "Окно поиска справочника не обнаружено"

    def chose_search_guide_window(self):
        if self.click_on_visible_element(GL.search_guide_window):
            sleep(0.5)
            pass
        else:
            assert False, "Строка поиска справочника не обнаружена"

    def add_button_list(self):
        if self.click_on_visible_element(GL.add_button_list):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка добавить на листе справчоника не найдена"

    def a_b_l_add_column(self):
        if self.click_on_visible_element(GL.a_b_l_add_column):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка добавить столбец не найдена"

    def column_type_object_type(self):
        if self.click_on_visible_element(GL.column_type_object_type):
            sleep(0.5)
            pass
        else:
            assert False, "Тип столбца Объект не обнаружен"

    def column_name_parser(self, key_name):
        if self.click_on_visible_element(GL.column_name_parser):
            sleep(0.5)
            self.send_keys_to_visible_element(GL.column_name_parser, key_name)
            sleep(0.5)
            pass
        else:
            assert False, "Поле имя для парсинга не обнаружено"

    def column_name_parser_for_meaning(self, key_name):
        if self.click_on_visible_element(GL.column_name_parser_for_meaning):
            sleep(0.5)
            self.send_keys_to_visible_element(GL.column_name_parser_for_meaning, key_name)
            sleep(0.5)
            pass
        else:
            assert False, "Поле имя для парсинга для назначения Значение не обнаружено"

    def column_add_button(self):
        if self.click_on_visible_element(GL.column_add_button):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка добавить столбец после настройки не обнаружена"

    def column_type_process_type(self):
        if self.click_on_visible_element(GL.column_type_process_type):
            sleep(0.5)
            pass
        else:
            assert False, "Выбор типа столбца Процесс не обнаружен"

    def column_type_attribute(self):
        if self.click_on_visible_element(GL.column_type_attribute):
            sleep(0.5)
            pass
        else:
            assert False, "Выбор типа столбца Атрибут не обнаружен"

    def column_attribute_obj_or_proc(self):
        if self.click_on_visible_element(GL.column_attribute_obj_or_proc):
            sleep(0.5)
            pass
        else:
            assert False, "Поле выбора между объектом или процессом для Атрибута не обнаружено"

    def column_attribute_o_or_p_choose(self, key_name):
        if self.click_on_visible_element(GL.column_attribute_o_or_p_choose):
            sleep(0.5)
            self.send_keys_to_visible_element(GL.column_attribute_o_or_p_choose, key_name)
            sleep(0.5)
            pass
        else:
            assert False, "Поле выбора конкретного объекта или процесса для Атрибута не найдено"

    def column_attribute_connect(self, key_name):
        if self.click_on_visible_element(GL.column_attribute_connect):
            sleep(0.5)
            self.send_keys_to_visible_element(GL.column_attribute_connect, key_name)
            sleep(0.5)
            pass
        else:
            assert False, "Поле связи объекта с другим объектом у Атрибута не обнаружено"

    def column_attribute_attribute_choose_for_object(self, key_name):
        if self.click_on_visible_element(GL.column_attribute_attribute_choose_for_object):
            sleep(0.5)
            self.send_keys_to_visible_element(GL.column_attribute_attribute_choose_for_object, key_name)
            sleep(0.5)
            pass
        else:
            assert False, "Поле выбора атрибута, привязанного к объекту не обнаружено"

    def column_attribute_attribute_choose_for_process(self, key_name):
        if self.click_on_visible_element(GL.column_attribute_attribute_choose_for_process):
            sleep(0.5)
            self.send_keys_to_visible_element(GL.column_attribute_attribute_choose_for_process, key_name)
            sleep(0.5)
            pass
        else:
            assert False, "Поле выбора атрибута, привязанного к процессу не обнаружено"

    def column_meaning(self):
        if self.click_on_visible_element(GL.column_meaning):
            sleep(0.5)
            pass
        else:
            assert False, "Выбор назначения колонки не обнаружен"

    def upload_button_list(self):
        if self.click_on_visible_element(GL.upload_button_list):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка загрузки справочника не обнаружена"

    def save_guide_button_list(self):
        if self.click_on_visible_element(GL.save_guide_button_list):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка сохранения справочника не обнаружена"

    def save_guide_button_confirm(self):
        if self.click_on_visible_element(GL.save_guide_button_confirm):
            sleep(0.5)
            pass
        else:
            assert False, "Кнопка подтверждения сохранения справочника не обнаружена"

    def check_uploaded_guide(self):
        check_list_type = 'Ствол'
        for i in range(4):
            text_of_check_list_type = self.attribute_of_visible_element(
                (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div > div > table > tbody > tr:nth-chil'
                                  'd(' + str(i + 1) + ') > td:nth-child(2) > div > div > div > div > div > input'), 'va'
                'lue')
            sleep(1)
            if not text_of_check_list_type == check_list_type:
                assert False, "Значения в колонках типа объекта не соответствуют должным"
            sleep(1)
        check_list_process = ['Передвижка БУ', 'Мобилизация БУ', 'Монтаж БУ', 'Передвижка БУ']
        for j in range(4):
            text_of_check_list_process = self.attribute_of_visible_element(
                (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div.jss74 > div > div > table > tbody > tr:nt'
                                  'h-child(' + str(j + 1) + ') > td:nth-child(3) > div > div > div > div > div > input'
                 ), 'value')
            sleep(1)
            if not text_of_check_list_process == check_list_process[j]:
                assert False, "Значения в колонках типового процесса не соответствуют должным"
            sleep(1)
        check_list_attribute = ['г.п. 225тн', 'г.п. 225тн', 'г.п. 250тн', 'г.п. 225тн']
        for g in range(4):
            text_of_check_list_attribute = self.attribute_of_visible_element(
                (By.CSS_SELECTOR, '#root > div > div:nth-child(3) >Хоро div > div > div > div > table > tbody > tr:nth-'
                                  'child(' + str(g + 1) + ') > td:nth-child(4) > div > input'), 'value')
            sleep(1)
            if not text_of_check_list_attribute == check_list_attribute[g]:
                assert False, "Значения в колонках атрибута не сооветствуют должным"
