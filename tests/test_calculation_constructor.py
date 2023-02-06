import allure
import pytest
from pages.calculation_constructor_page import CalculationConstructorPage as CCPage
from time import sleep


class TestCalculationConstructor:

    @allure.feature("Удаление МК с фронта")
    @allure.story("Удаление всех имеющихся на стенде МК")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.c_c_clear_mb
    def test_clear_stand(self, sign_in_to_stand):
        with allure.step("Прохождение авторизации на стенде"):
            page = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            CCPage.move_to_calculation_constructor_page(page)
            sleep(1)
            CCPage.is_page_calculation_page(page)
        with allure.step("Очистка мастер-книг со стенда"):
            CCPage.delete_all_masterbooks(page)

    @allure.feature("Парсер МК")
    @allure.story("Загрузка всех имеющихся МК на стенд и проверка, что все загрузилось корректно")
    @pytest.mark.sandbox
    def test_parser(self, sign_in_to_stand):
        with allure.step("Прохождение авторизации на стенде"):
            page = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            CCPage.move_to_calculation_constructor_page(page)
            sleep(1)
            CCPage.is_page_calculation_page(page)
        with allure.step("Очистка мастер-книг со стенда"):
            CCPage.delete_all_masterbooks(page)
        with allure.step("Загрузка мастер-книги на стенд"):
            # Функция с загрузкой МК и проверкой, что все кейсы/консолидации загрузились успешно
            pass

    @allure.feature("Ядро расчетов")
    @allure.story("Выбор случайной МК, случайного кейса и расчет с первыми попавшимися макрой и ФЭМ")
    @pytest.mark.sandbox
    def test_calculation(self, sign_in_to_stand):
        pass
