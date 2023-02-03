import allure
import pytest

#       Сделать параметризованные тесты
#       Сделать clear_masterbooks
#       Прописать base_page


class TestSandbox:
    # Пример теста
    def any_new_test(self, sign_in_to_stand):
        with allure.step("Прохождение авторизации на стенде"):
            _ = sign_in_to_stand

    @allure.feature('Авторизация')
    @allure.story('Прохождение авторизации на стенд')
    @pytest.mark.sandbox
    def test_sandbox(self, sign_in_to_stand):
        with allure.step("Прохождение авторизации на стенде"):
            _ = sign_in_to_stand
            assert False, "Поломка чет"
        pass
