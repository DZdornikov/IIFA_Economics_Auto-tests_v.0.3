import pytest
import subprocess
from config import main_dir, ffmpeg_path, record_video_mode, current_stand
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import listdir, remove, path
from datetime import datetime as dt
from time import sleep

# Переменные
report_dir = fr'{main_dir}\video_reports'                                           # Берем путь в директорию с видео


# Set_up & Tear_down функция. Запускает браузер и тушит его в самом конце теста
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=(Service(ChromeDriverManager().install())))
    driver.maximize_window()
    yield driver
    driver.quit()


# Функция для очистки папки с видео. ПОСЛЕДСТВИЯ НЕОБРАТИМЫ!!!
# Запуск только в PyCharm. Нужно снять комментарий, запустить, закомментировать. Если не закомментировать, то будет
# очень плохо
# @pytest.mark.novideo
# def test_clear_video_dir():
#     for f in listdir(report_dir):
#         remove(path.join(report_dir, f))

# Функция для автозаписи и сохранения видео
@pytest.fixture(scope="function", autouse=True)
def record_video(request):
    sleep(10)
    """Fixture records video for all tests and saves it if test failed"""
    if 'novideo' in request.keywords:
        yield
    else:
        mode = record_video_mode
        if (not path.exists(ffmpeg_path)) or (mode == 'none'):
            yield
        else:
            outfile = f"{report_dir}\\{request.node.name}_{dt.now().strftime('%H_%M_%S')}.mp4"
            cmd = f'{ffmpeg_path} -f gdigrab -framerate ntsc -video_size 1920x1080 -i desktop {outfile}'
            ffmpeg_process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                              stdin=subprocess.PIPE)
            tests_failed_before_module = request.session.testsfailed
            yield
            tests_failed_during_module = request.session.testsfailed - tests_failed_before_module

            ffmpeg_process.communicate(input=b'q')
            ffmpeg_process.wait()

            if (tests_failed_during_module == 0) and (mode == 'failed'):
                # Remove video file if test passed
                remove(outfile)

# Функция для входа на стенд. Запускает модуль "Экономика" по адресу стенда, проходит KeyCloak
@pytest.fixture()
def sign_in_to_stand(driver, stand=current_stand):
    pass
