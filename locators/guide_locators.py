from selenium.webdriver.common.by import By


class GuideLocators:

    # Перейти на страницу справочников
    move_to_guide_page = (By.CSS_SELECTOR, "#root > div > header > div > a:nth-child(6)")
    # Создать группу справочников
    create_guide_group = (By.CSS_SELECTOR, "#root > div > div:nth-child(3) > div > div > div > div:nth-child(1) > svg")
    # Окно ввода названия группы справочника
    guide_name_print = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > input")
    # Добавить группу справочников или справочник
    guide_group_add_button = (By.CSS_SELECTOR, "body > div > div > div > div > button:nth-child(2)")
    # Открыть дополнительное меню
    open_menu = (By.CSS_SELECTOR, "#root > div > div:nth-child(3) > div > div > div > div > nav:nth-child(1) > div > bu"
                                  "tton")
    # Удалить группу справочников
    delete_guide_group = (By.CSS_SELECTOR, "#description-menu > div > ul > li:nth-child(3)")
    # Кнопка добавить на листе
    add_button_list = (By.CSS_SELECTOR, "#root > div > div:nth-child(3) > div > div > div > div > div.MuiBox-root.css-u"
                                        "4p24i > div:nth-child(1) > button")
    # Кнопка загрузить справочник
    upload_button_list = (By.CSS_SELECTOR, "#root > div > div:nth-child(3) > div > div > div > div > div > div:nth-chil"
                                           "d(4) > button")
    # Чекбокс оператора
    operator_switch = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > label > span > span")
    # Создать колонку с типом "Дата"
    type_column_date = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > button:nth-child(1)")
    # Создать колонку с типом "Строка"
    type_column_string = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > button:nth-child(2)")
    # Создать колонку с типом "Число"
    type_column_number = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > button:nth-child(3)")
    # Имя колонки
    column_name = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > div > input")
    # Выбор типа колонки
    column_type_choose = (By.CSS_SELECTOR, "#menu- > div > ul > li:nth-child(1)")
    # Значение колонки
    column_purpose = (By.CSS_SELECTOR, "#type_structure_select")
    # Размерность колонки
    column_dimension = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > div > div > input")
    # Поле поиска справочника
    search_guide_window = (By.CSS_SELECTOR, "#root > div > div:nth-child(3) > div > div > div > div > div > input")
    # Кнопка добавить колонку
    a_b_l_add_column = (By.CSS_SELECTOR, "body > div > div > ul > li")
    # Выбор типа объекта из назначения "Ключ"
    column_type_object_type = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > button:nth-child(2)")
    # Выбор имени колонки для парсинга назначения "Ключ"
    column_name_parser = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > div:nth-child(2) > input:n"
                                           "th-child(1)")
    # Выбор имени колонки для парсинга назначения "Значение"
    column_name_parser_for_meaning = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div:nth-child(2) > d"
                                                       "iv:nth-child(2) > input:nth-child(1)")
    # Кнопка добавления столбца
    column_add_button = (By.CSS_SELECTOR, "body > div > div > div > div > div > button:nth-child(2)")
    # Выбор типового процесса из назначения "Ключ"
    column_type_process_type = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > button:nth-child(3)")
    # Выбор атрибута из назначения "Ключ"
    column_type_attribute = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > button:nth-child(1)")
    # Выбор между объектом и процессом для связи с атрибутом
    column_attribute_obj_or_proc = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div:nth-child(2) > div"
                                                     " > div > input")
    # Выбор нужного типа объекта или процесса для связи с атрибутом
    column_attribute_o_or_p_choose = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div:nth-child(3) > d"
                                                       "iv > div > input")
    # Выбор связи для объекта для связи с атрибутом
    column_attribute_connect = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div:nth-child(4) > div > d"
                                                 "iv > input")
    # Выбор атрибута для создания колонки
    column_attribute_attribute_choose_for_object = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div:nt"
                                                                     "h-child(5) > div > div > input")
    column_attribute_attribute_choose_for_process = (By.CSS_SELECTOR, "body > div > div > div > div > div > div > div:n"
                                                                      "th-child(4) > div > div > input")
    # Назначение колонки "Ключ" или "Значение"
    column_meaning = (By.CSS_SELECTOR, "body > div:nth-child(4) > div > div > div > div:nth-child(1) > div > div > div "
                                       "> div")
    # Нажимает на кнопку сохранить справочник
    save_guide_button_list = (By.CSS_SELECTOR, "#root > div > div:nth-child(3) > div > div > div > div > div > div:nth-"
                                               "child(3) > button")
    # Подтверждает сохранение справочника
    save_guide_button_confirm = (By.CSS_SELECTOR, "body > div > div > div > div > button:nth-child(2)")
    # Кнопка добавить справочник или версию справочника
    add_guide_button = (By.CSS_SELECTOR, "#description-menu > div > ul > li:nth-child(1)")
