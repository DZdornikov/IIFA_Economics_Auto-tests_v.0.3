from os import path
from logging import INFO, CRITICAL, DEBUG, ERROR, WARNING                               # Для выбора уровня логирования

# СТРОКИ, КОТОРЫЕ ЛУЧШЕ НЕ ТРОГАТЬ

# Адресная книга
mskdev = 'http://mskdev.nntc.pro/economics/'
gpn = 'http://gpn.mskdev.nntc.pro/economics/'
generated_dev = "http://generated.dev.nntc.pro/economics/"
genrestest = 'http://genrestest.nntc.pro/economics/'

# Функциональное
main_dir = path.dirname(__file__)

# СТРОКИ ЗАПОЛНЯЮТСЯ ПОЛЬЗОВАТЕЛЕМ

tester_name = "Ваня Пупкин"                                                             # Имя-фамилия тестировщика
ffmpeg_path = fr'{main_dir}\путь к ffmpeg.exe'                                          # Путь к ffmpeg.exe
record_video_mode = "all"                                   # Режим записи видео. Поддерживаемые: 'all'/'none'/'failed'
downloads_dir = fr"C:\Users\dpodolny\Downloads"                                         # Путь к папке загрузок
current_stand = genrestest                                                              # Выбор стенда для работы
logger_level = DEBUG                                                                    # Уровень логирования
