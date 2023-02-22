from selenium.webdriver.common.by import By


class CalculationConstructorLocators:
    # Общие
    move_to_calculation_constructor_page_button = (By.CSS_SELECTOR, "#root > div > header > div > a:nth-child(7)")
    start_calculation_button = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div > div > div > div > '
                                                 'div.MuiGrid-root.MuiGrid-container.MuiGrid-item.css-8x8291 > div > bu'
                                                 'tton > svg')
    first_notification = (By.CSS_SELECTOR, '#root > div.Toastify > div > div')

    # МК
    first_MB = (By.CSS_SELECTOR, "#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div"
                                 ".MuiGrid-root.css-rfnosa > div:nth-child(2)")
    additional_menu_first_MB = (By.CSS_SELECTOR, "#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div >"
                                                 " div > div > div > div:nth-child(2) > div > div.MuiAccordionSummary-c"
                                                 "ontent.MuiAccordionSummary-contentGutters.css-s2q1rt > button")
    second_button_MB = (By.CSS_SELECTOR, "#description-menu > div > ul > li:nth-child(2)")
    confirm_delete_button_MB = (By.CSS_SELECTOR, "body > div > div.MuiBox-root.css-1xt3qe > div > button:nth-child(1)")
    upload_MB = (By.CSS_SELECTOR, "#root > div.MuiBox-root.css-18cq61h > div:nth-child(3) > div > div > div:nth-child(1"
                                  ") > div > div > div > div.MuiGrid-root.css-rfnosa > div > button > input[type=file]")

    # ФЭМ и Макропараметры
    open_FEM_menu_button = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div > div'
                                             ' > div > div:nth-child(2) > div > div > svg')
    open_Macro_menu_button = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div > d'
                                               'iv > div > div:nth-child(3) > div > div > svg')
    first_FEM = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div > div > div > di'
                                  'v:nth-child(2) > div > div > div > div > div > ul > li:nth-child(1) > div')
    additional_menu_first_FEM = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div '
                                                  '> div > div > div > div.MuiCollapse-root.MuiCollapse-vertical.MuiCol'
                                                  'lapse-entered.css-c4sutr > div > div > div > div > ul > li:nth-child'
                                                  '(1) > button')
    upload_FEM = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div > div > div > d'
                                   'iv > div > div > div > div > input[type=file]')
    delete_first_FEM = (By.XPATH, '/html/body/div[3]/div[3]/ul/li/div/span')
    first_Macro = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div > div > div > '
                                    'div > div.MuiCollapse-root.MuiCollapse-vertical.MuiCollapse-entered.css-c4sutr > d'
                                    'iv > div > div > div > ul > li')
    additional_menu_first_Macro = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > di'
                                                    'v > div > div > div > div.MuiCollapse-root.MuiCollapse-vertical.Mu'
                                                    'iCollapse-entered.css-c4sutr > div > div > div > div > ul > li > b'
                                                    'utton')
    upload_Macro = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div > div > div >'
                                     ' div > div > div > div > div > input[type=file]')

    # Условия расчета
    open_calculation_conditions_menu_button = (By.CSS_SELECTOR,
                                               '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div > d'
                                               'iv > div > div:nth-child(1) > div > div > svg')
    conditions_project_start_input = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) >'
                                                       ' div > div > div > div > div.MuiCollapse-root.MuiCollapse-verti'
                                                       'cal.MuiCollapse-entered.css-c4sutr > div > div > div > div > di'
                                                       'v > div:nth-child(1) > div > div > input')
    conditions_project_start_button = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) '
                                                        '> div > div > div > div > div.MuiCollapse-root.MuiCollapse-ver'
                                                        'tical.MuiCollapse-entered.css-c4sutr > div > div > div > div >'
                                                        ' div > div:nth-child(1) > div > div > div > button')
    conditions_infl_start_date_input = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3)'
                                                         ' > div > div > div > div > div.MuiCollapse-root.MuiCollapse-v'
                                                         'ertical.MuiCollapse-entered.css-c4sutr > div > div > div > di'
                                                         'v > div > div:nth-child(2) > div > div > input')
    conditions_infl_start_date_button = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3'
                                                          ') > div > div > div > div > div.MuiCollapse-root.MuiCollapse'
                                                          '-vertical.MuiCollapse-entered.css-c4sutr > div > div > div >'
                                                          ' div > div > div:nth-child(2) > div > div > div > button')
    conditions_disc_start_input = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > di'
                                                    'v > div > div > div > div.MuiCollapse-root.MuiCollapse-vertical.Mu'
                                                    'iCollapse-entered.css-c4sutr > div > div > div > div > div > div:n'
                                                    'th-child(3) > div > div > input')
    conditions_disc_start_button = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > d'
                                                     'iv > div > div > div > div.MuiCollapse-root.MuiCollapse-vertical.'
                                                     'MuiCollapse-entered.css-c4sutr > div > div > div > div > div > di'
                                                     'v:nth-child(3) > div > div > div > button')
    conditions_econom_limit_date_input = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child('
                                                           '3) > div > div > div > div > div.MuiCollapse-root.MuiCollap'
                                                           'se-vertical.MuiCollapse-entered.css-c4sutr > div > div > di'
                                                           'v > div > div > div:nth-child(4) > div > div > input')
    conditions_econom_limit_date_button = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-child'
                                                            '(3) > div > div > div > div > div.MuiCollapse-root.MuiColl'
                                                            'apse-vertical.MuiCollapse-entered.css-c4sutr > div > div >'
                                                            ' div > div > div > div:nth-child(4) > div > div > div > bu'
                                                            'tton')
    conditions_calculation_horizon_input = (By.CSS_SELECTOR,
                                            '#root > div > div:nth-child(3) > div > div > div:nth-child(3) > div > div '
                                            '> div > div > div.MuiCollapse-root.MuiCollapse-vertical.MuiCollapse-entere'
                                            'd.css-c4sutr > div > div > div > div > div > div:nth-child(5) > div > div '
                                            '> input')
    conditions_date_type_econom_limit_div = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div:nth-chi'
                                                              'ld(3) > div > div > div > div > div.MuiCollapse-root.Mui'
                                                              'Collapse-vertical.MuiCollapse-entered.css-c4sutr > div >'
                                                              ' div > div > div > div > div:nth-child(6) > div > div')
