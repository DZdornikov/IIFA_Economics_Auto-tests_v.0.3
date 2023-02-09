import allure
import pytest
from pages.guide_page import GuidePage as GP
from time import sleep
from pages.base_page import BasePage as BP              # Для рефреша страницы
import keyboard                                         # Для функционирования с выпадающими окнами без селекторов


class TestGuideUploadRigDuration:

    @allure.feature("Проверка загрузки справочника")
    @allure.story("Чистит стенд, создаёт справочник, его шапку, а затем загружает excel, сверяя с захардкоженными данны"
                  "ми, после чего сохраняет результат")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.guide
    def test_rig_duration(self, sign_in_to_stand):
        with allure.step("Прохождение авторизации на стенде"):
            sign_in = sign_in_to_stand
            GP.move_to_guide_page(sign_in)
            sleep(1)
            GP.is_page_guide_page(sign_in)
        with allure.step("Создание и открытие нужного справочника"):
            GP.search_guide_window(sign_in)
            GP.open_menu(sign_in)
            GP.delete_guide_group(sign_in)
            GP.guide_group_or_guide_add_button(sign_in)
            GP.chose_search_guide_window(sign_in)
            keyboard.press_and_release('ctrl+a, delete')
            GP.create_guide_group(sign_in)
            GP.guide_group_name_print(sign_in)
            GP.guide_group_or_guide_add_button(sign_in)
            GP.open_menu(sign_in)
            GP.add_guide(sign_in)
            GP.guide_group_name_print(sign_in)
            GP.guide_group_or_guide_add_button(sign_in)
        with allure.step("Создание столбца с типом Тип объекта"):
            GP.add_button_list(sign_in)
            GP.a_b_l_add_column(sign_in)
            GP.column_type_object_type(sign_in)
            GP.column_name_parser(sign_in, 'ObjectType')
            GP.column_add_button(sign_in)
        with allure.step("Создание столбца с типом Типовой процесс"):
            GP.add_button_list(sign_in)
            GP.a_b_l_add_column(sign_in)
            GP.column_type_process_type(sign_in)
            GP.column_name_parser(sign_in, 'ProcessType')
            GP.column_add_button(sign_in)
        # with allure.step("Создание атрибута со связью через объект"):
            # Добавление атрибута со связью через объект
            #        GP.add_button_list(sign_in, log_name)
            #        GP.a_b_l_add_column(sign_in, log_name)
            #        GP.column_type_attribute(sign_in, log_name)
            #        GP.column_name_parser(sign_in, log_name, 'WellOrder')
            #        GP.column_attribute_obj_or_proc(sign_in, log_name)
            #        keyboard.press_and_release('down, enter')
            #        GP.column_attribute_o_or_p_choose(sign_in, log_name, 'Ствол')
            #        keyboard.press_and_release('down, enter')
            #        GP.column_attribute_connect(sign_in, log_name, 'Скважина')
            #        keyboard.press_and_release('down, enter')
            #        GP.column_attribute_attribute_choose_for_object(sign_in, log_name, 'Порядок')
            #        keyboard.press_and_release('down, enter')
            #        GP.column_add_button(sign_in, log_name)
            #        GP.add_button_list(sign_in, log_name)
            #        GP.a_b_l_add_column(sign_in, log_name)
            #        GP.column_type_attribute(sign_in, log_name)
            #        GP.column_name_parser(sign_in, log_name, 'MobilizationMarker')
            #        GP.column_attribute_obj_or_proc(sign_in, log_name)
            #        keyboard.press_and_release('down, enter')
            #        GP.column_attribute_o_or_p_choose(sign_in, log_name, 'Ствол')
            #        keyboard.press_and_release('down, down, enter')
            #        GP.column_attribute_attribute_choose_for_object(sign_in, log_name, 'Признак')
            #        keyboard.press_and_release('down, down, enter')
            #        GP.column_add_button(sign_in, log_name)
        with allure.step("Добавление атрибута со связью через процесс"):
            GP.add_button_list(sign_in)
            GP.a_b_l_add_column(sign_in)
            GP.column_type_attribute(sign_in)
            GP.column_name_parser(sign_in, 'TypeRig')
            GP.column_attribute_obj_or_proc(sign_in)
            keyboard.press_and_release('down, down, enter')
            GP.column_attribute_o_or_p_choose(sign_in, 'Переезд Буровой')
            keyboard.press_and_release('down, enter')
            GP.column_attribute_attribute_choose_for_process(sign_in, 'Тип буровой')
            keyboard.press_and_release('down, enter')
            GP.column_add_button(sign_in)
            #        GP.add_button_list(sign_in, log_name)
            #        GP.a_b_l_add_column(sign_in, log_name)
            #        GP.column_type_attribute(sign_in, log_name)
            #        GP.column_name_parser(sign_in, log_name, 'TypeMoveRig')
            #        GP.column_attribute_obj_or_proc(sign_in, log_name)
            #        keyboard.press_and_release('down, down, enter')
            #        GP.column_attribute_o_or_p_choose(sign_in, log_name, 'Переезд Буровой')
            #        keyboard.press_and_release('down, enter')
            #        GP.column_attribute_attribute_choose_for_process(sign_in, log_name, 'Тип перемещения')
            #        keyboard.press_and_release('down, enter')
            #        GP.column_add_button(sign_in, log_name)
        # with allure.step("Добавление колонки с типом число"):
            #        GP.add_button_list(sign_in, log_name)
            #        GP.a_b_l_add_column(sign_in, log_name)
            #        GP.column_purpose(sign_in, log_name)
            #        keyboard.press_and_release('down, enter')
            #        GP.column_meaning(sign_in, log_name)
            #        GP.type_column_number(sign_in, log_name)
            #        GP.column_name(sign_in, log_name, 'Constant')
            #        GP.column_name_parser_for_meaning(sign_in, log_name, 'Constant')
            #        GP.column_add_button(sign_in, log_name)
        with allure.step("Загрузка справочника"):
            GP.upload_button_list(sign_in)
            sleep(1)
            keyboard.write('RigDuration')
            sleep(1)
            keyboard.press_and_release('down, enter')
            sleep(3)
            BP.refresh(sign_in)
            sleep(5)
        with allure.step("Сверка загруженной версии справочника"):
            GP.check_uploaded_guide(sign_in)
        with allure.step("Сохранение справочника"):
            GP.save_guide_button_list(sign_in)
            GP.save_guide_button_confirm(sign_in)
            BP.refresh(sign_in)
        with allure.step("Повторная сверка загруженной версии"):
            GP.check_uploaded_guide(sign_in)
