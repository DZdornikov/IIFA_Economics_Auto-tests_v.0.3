import allure
import pytest
import subprocess
import psutil
from config import main_dir, ffmpeg_path, current_stand
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import listdir, remove, path
from shutil import copy
from datetime import datetime as dt
from pages.sign_in_page import SignInPage
from functools import update_wrapper
from time import sleep

# Переменные
video_reports_dir = fr'{main_dir}\video_reports'                            # Путь к директории видео тестов
allure_report_dir = fr'{main_dir}\tests\allure-report'
allure_results_dir = fr'{main_dir}\tests\allure-results'


# Set_up & Tear_down функция. Запускает браузер и тушит его в самом конце теста
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=(Service(ChromeDriverManager().install())))
    driver.maximize_window()
    yield driver
    driver.quit()


# Wrapper для записи видео во время работы теста
# Дропается если тест провальный
def recorder_wrapper(func):
    def func_wrapper(*args, **kwargs):
        # Проверка, что у нас не гоняется ffmpeg в фоне
        for proc in psutil.process_iter():
            name = proc.name()
            if name == "ffmpeg.exe":
                proc.kill()
        outfile = f"{video_reports_dir}\\{func.__name__}_{dt.now().strftime('%H_%M_%S')}.mp4"
        if path.exists(outfile):
            remove(outfile)
        cmd = f'{ffmpeg_path} -f gdigrab -framerate ntsc -video_size 1920x1080 -i desktop {outfile}'
        ffmpeg_process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                          stdin=subprocess.PIPE)
        try:
            func(*args, **kwargs)  # No return values
            ffmpeg_process.communicate(input=b'q')
            ffmpeg_process.wait()
            sleep(1)
            allure.attach.file(outfile, attachment_type=allure.attachment_type.MP4)
            ffmpeg_process.kill()
        except AssertionError as ae:
            print(f"Assertion failed: {str(ae)}")
            ffmpeg_process.communicate(input=b'q')
            ffmpeg_process.wait()
            sleep(1)
            allure.attach.file(outfile, attachment_type=allure.attachment_type.MP4)
            ffmpeg_process.kill()
            raise
        except Exception as e:
            print(f"Unknown error: {str(e)}")
            ffmpeg_process.communicate(input=b'q')
            ffmpeg_process.wait()
            sleep(1)
            allure.attach.file(outfile, attachment_type=allure.attachment_type.MP4)
            ffmpeg_process.kill()
            raise

    update_wrapper(func_wrapper, func)
    return func_wrapper


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    item._obj = recorder_wrapper(item._obj)


# Функция для входа на стенд. Запускает модуль "Экономика" по адресу стенда, проходит KeyCloak
@pytest.fixture()
def sign_in_to_stand(driver, stand=current_stand):
    sign_in_page = SignInPage(driver, stand)
    sign_in_page.open()
    sign_in_page.keycloak_authorization()
    return sign_in_page


# Функция для очистки папки с видео. ПОСЛЕДСТВИЯ НЕОБРАТИМЫ!!!
# Запуск только в PyCharm. Нужно снять комментарий, запустить, закомментировать. Если не закомментировать, то будет
# очень плохо
# def test_novideo_clear_video_dir():
#     for f in listdir(video_reports_dir):
#         remove(path.join(video_reports_dir, f))


# Функция удаляет устаревшую историю прогона тестов и заменяет на новую везде, где нужно
@pytest.fixture(autouse=True)
def test_append_report_history():
    history_in_allure_res = fr"{allure_results_dir}\history"
    history_in_allure_rep = fr"{allure_report_dir}\history"
    history_in_main_dir = fr"{main_dir}\history"

    # Очистка устаревшей истории
    for f in listdir(history_in_allure_res):
        remove(path.join(history_in_allure_res, f))

    for f in listdir(history_in_main_dir):
        remove(path.join(history_in_main_dir, f))

    # Копирование обновленной истории
    for f in listdir(history_in_allure_rep):
        copy(path.join(history_in_allure_rep, f), history_in_main_dir)
        copy(path.join(history_in_allure_rep, f), history_in_allure_res)
