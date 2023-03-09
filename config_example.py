from os import path

# СТРОКИ, КОТОРЫЕ ЛУЧШЕ НЕ ТРОГАТЬ

# Адресная книга
mskdev = 'http://mskdev.nntc.pro/economics/'
gpn = 'http://gpn.mskdev.nntc.pro/economics/'
generated_dev = "http://generated.dev.nntc.pro/economics/"
genrestest = 'http://genrestest.nntc.pro/economics/'
demorospan = 'http://demo.rospan.iifa.ru/economics/'

# Функциональное
main_dir = path.dirname(__file__)

# СТРОКИ ЗАПОЛНЯЮТСЯ ПОЛЬЗОВАТЕЛЕМ

tester_name = "Ваня Пупкин"                                                             # Имя-фамилия тестировщика
ffmpeg_path = fr'{main_dir}\путь к ffmpeg.exe'                                          # Путь к ffmpeg.exe
downloads_dir = fr"ПУТЬ К ПАПКЕ ЗАГРУЗОК"                                               # Путь к папке загрузок
current_stand = genrestest                                                              # Выбор стенда для работы
