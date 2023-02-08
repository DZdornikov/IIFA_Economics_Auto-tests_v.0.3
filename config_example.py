from os import path

# СТРОКИ, КОТОРЫЕ ЛУЧШЕ НЕ ТРОГАТЬ

# Адресная книга
mskdev = 'http://mskdev.nntc.pro/economics/'
gpn = 'http://gpn.mskdev.nntc.pro/economics/'
generated_dev = "http://generated.dev.nntc.pro/economics/"
genrestest = 'http://genrestest.nntc.pro/economics/'

# СТРОКИ ЗАПОЛНЯЮТСЯ ПОЛЬЗОВАТЕЛЕМ

tester_name = "Ваня Пупкин"
main_dir = path.dirname(__file__)
# Путь к ffmpeg.exe
ffmpeg_path = fr'{main_dir}\tools\ПУТЬ К ffmpeg.exe'
# Режим записи видео. Поддерживаемые: 'all'/'none'/'failed'
record_video_mode = "all"
# Путь к папке загрузок
downloads_dir = fr"ПУТЬ К ПАПКЕ ЗАГРУЗОК"
# Выбор стенда для работы
current_stand = gpn
