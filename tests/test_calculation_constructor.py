import allure
import pytest


class TestCalculationConstructor:

    @allure.feature("Парсер МК")
    @allure.story("Загрузка всех имеющихся МК на стенд и проверка, что все загрузилось корректно")
    def test_parser(self, sign_in_to_stand):
        with allure.step("Прохождение авторизации на стенде"):
            _ = sign_in_to_stand
        with allure.step("Переход в конструктор расчетов"):
            # Простая функция с переходом и проверкой успешности перехода
            pass
        with allure.step("Очистка мастер-книг со стенда"):
            # Функция с циклом удаления МК со стенда
            pass
        with allure.step("Загрузка мастер-книги на стенд"):
            # Функция с загрузкой МК и проверкой, что все кейсы/консолидации загрузились успешно
            pass
    pass
