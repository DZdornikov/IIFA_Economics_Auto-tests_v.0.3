import allure
import pytest
from config import tester_name
from pages.calculation_constructor_page import CalculationConstructorPage as CCPage
from files.files_list import CalculationConstructorFilesList as CCFiles
from time import sleep

# TODO:
#       ПРОТЕСТИТЬ ТЕСТ НА ПАРСЕР
#       ДОПИСАТЬ ТЕСТ ЯДРА РАСЧЕТОВ
#       заменить assert на raise exception там, где это нужно


class TestCalculationConstructor:

    @allure.feature("Удаление МК с фронта")
    @allure.story("Удаление всех имеющихся на стенде МК")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(f"Тест запустил - {tester_name}")
    @pytest.mark.calculacion_constructor
    def test_clear_stand(self, sign_in_to_stand):
        with allure.step("Прохождение авторизации на стенде"):
            page = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            CCPage.move_to_calculation_constructor_page(page)
            sleep(1)
            CCPage.is_page_calculation_page(page)
        with allure.step("Очистка мастер-книг со стенда"):
            sleep(4)    # МК появляются не мгновенно
            CCPage.delete_all_masterbooks(page)

    @allure.feature("Загрузка МК на фронт")
    @allure.story("Загрузка всех имеющихся МК на стенд и проверка, что все загрузилось корректно")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description(f"Тест запустил - {tester_name}")
    @pytest.mark.calculacion_constructor
    @pytest.mark.parametrize('mb_name', [CCFiles.MB_GEE_filename, CCFiles.MB_KUV_filename, CCFiles.MB_CNT_filename,
                                         CCFiles.MB_YUUNG_filename, CCFiles.MB_YUUNG_BUR_filename,
                                         CCFiles.MB_YAG_filename])
    def test_parser(self, sign_in_to_stand, mb_name):
        with allure.step("Прохождение авторизации на стенде"):
            page = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            CCPage.move_to_calculation_constructor_page(page)
            sleep(1)
            CCPage.is_page_calculation_page(page)
        with allure.step("Очистка мастер-книг со стенда"):
            CCPage.delete_all_masterbooks(page)
        with allure.step(f'Загрузка мастер-книги на стенд'):
            CCPage.upload_mb(page, mb_name, timer=300)

    @allure.feature("Ядро расчетов, выгрузка отчета")
    @allure.story("Выбор случайной МК, случайного кейса и расчет с первыми попавшимися макрой и ФЭМ. "
                  "Переход в отчеты и скачивание файла.")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description(f"Тест запустил - {tester_name}")
    @pytest.mark.calculacion_constructor
    def test_calculation(self, sign_in_to_stand):
        with allure.step("Прохождение авторизации на стенде"):
            page = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            CCPage.move_to_calculation_constructor_page(page)
            sleep(1)
            CCPage.is_page_calculation_page(page)
        with allure.step("Расчет с случайным кейсом, первыми попавшимися макрой и ФЭМ"):
            pass
