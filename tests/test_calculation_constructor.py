import allure
import pytest
from config import tester_name, current_stand
from pages.calculation_constructor_page import CalculationConstructorPage as CCPage
from files.files_list import CalculationConstructorFilesList as CCFiles
from time import sleep
from datetime import datetime as dt


# TODO: ВШИТЬ В ТЕСТЫ ДАТУ ПРОГОНА? ИЛИ МОЖНО ЕЕ И ДАЛЬШЕ ИЗ ВИДЕО БРАТЬ?
class TestCalculationConstructor:

    @allure.title("Удаление МК с фронта")
    @allure.feature("Удаление МК с фронта")
    @allure.story("Удаление всех имеющихся на стенде МК")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(f"Тест запустил - {tester_name}. \nСтенд, на котором запускался тест - {current_stand}\nДата "
                        f"запуска: {dt.now()}")
    @pytest.mark.calculacion_constructor
    def test_clear_stand(self, sign_in_to_stand):
        with allure.step("Прохождение авторизации на стенде"):
            page = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            CCPage.move_to_calculation_constructor_page(page)
            sleep(1)
            CCPage.is_page_calculation_page(page)
        with allure.step("Очистка мастер-книг со стенда"):
            sleep(4)
            CCPage.delete_all_masterbooks(page)

    @allure.title("Тест загрузки МК")
    @allure.feature("Загрузка МК на фронт")
    @allure.story("Загрузка всех имеющихся МК на стенд и проверка, что все загрузилось корректно")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description(f"Тест запустил - {tester_name}. \nСтенд, на котором запускался тест - {current_stand}\nДата "
                        f"запуска: {dt.now()}")
    @pytest.mark.calculacion_constructor
    @pytest.mark.parametrize('mb_name', [CCFiles.MB_GEE_filename, CCFiles.MB_KUV_filename, CCFiles.MB_CNT_filename,
                                         CCFiles.MB_YUUNG_filename, CCFiles.MB_YAG_filename,
                                         CCFiles.MB_YUUNG_BUR_filename])
    def test_parser(self, sign_in_to_stand, mb_name, clear_after_upload=False):
        with allure.step("Прохождение авторизации на стенде"):
            page = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            CCPage.move_to_calculation_constructor_page(page)
            sleep(1)
            CCPage.is_page_calculation_page(page)
        if clear_after_upload:
            with allure.step("Очистка мастер-книг со стенда"):
                CCPage.delete_all_masterbooks(page)
        with allure.step(f'Загрузка мастер-книги на стенд'):
            CCPage.upload_mb(page, mb_name)

    @allure.title("Расчет случайного кейса")
    @allure.feature("Ядро расчетов, выгрузка отчета")
    @allure.story("Выбор случайной МК, случайного кейса и расчет с первыми попавшимися макрой и ФЭМ. "
                  "Переход в отчеты и скачивание файла.")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description(f"Тест запустил - {tester_name}. \nСтенд, на котором запускался тест - {current_stand}\nДата "
                        f"запуска: {dt.now()}")
    @pytest.mark.calculacion_constructor
    def test_calculation(self, sign_in_to_stand):
        with allure.step("Прохождение авторизации на стенде"):
            page = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            CCPage.move_to_calculation_constructor_page(page)
            sleep(1)
            CCPage.is_page_calculation_page(page)
        with allure.step("Расчет с случайным кейсом, первыми попавшимися макрой и ФЭМ"):
            CCPage.calculate_random_case(page)

    @allure.title("Удаление и загрузка ФЭМ на стэнд")
    @allure.feature("Запросы в минио, загрузка, хранение, удаление файлов xml-формата")
    @allure.story("Удаление ФЭМ со стенда, загрузка, проверка что все ок. Проверяется по количеству, имя файлов не "
                  "проверяется")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description(f"Тест запустил - {tester_name}. \nСтенд, на котором запускался тест - {current_stand}\nДата "
                        f"запуска: {dt.now()}")
    @pytest.mark.calculacion_constructor
    @pytest.mark.parametrize('fem_file', [CCFiles.FEM_NDPI_dir, CCFiles.FEM_NDD_dir])
    def test_delete_and_upload_fem(self, sign_in_to_stand, fem_file):
        with allure.step("Прохождение авторизации на стенде"):
            page = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            CCPage.move_to_calculation_constructor_page(page)
            sleep(1)
            CCPage.is_page_calculation_page(page)
        with allure.step("Удаление всех ФЭМ"):
            CCPage.delete_all_fem(page)
        with allure.step("Загрузка всех ФЭМ"):
            CCPage.upload_fem(page, fem_file)

    @allure.title("Удаление и загрузка макропараметров на стэнд")
    @allure.feature("Запросы в минио, загрузка, хранение, удаление файлов las-формата")
    @allure.story("Удаление макропараметров со стенда, загрузка, проверка что все ок. Проверяется по количеству, имя "
                  "файлов не проверяется")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description(f"Тест запустил - {tester_name}. \nСтенд, на котором запускался тест - {current_stand}\nДата "
                        f"запуска: {dt.now()}")
    @pytest.mark.calculacion_constructor
    def test_delete_and_upload_macro(self, sign_in_to_stand, macro_file=CCFiles.macro_dir):
        with allure.step("Прохождение авторизации на стенде"):
            page = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            CCPage.move_to_calculation_constructor_page(page)
            sleep(1)
            CCPage.is_page_calculation_page(page)
        with allure.step("Удаление макропараметров"):
            CCPage.delete_all_macro(page)
        with allure.step("Загрузка макропараметров"):
            CCPage.upload_macro(page, macro_file)
