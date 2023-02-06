from selenium.webdriver.common.by import By


class CalculationConstructorLocators:
    move_to_calculation_constructor_page_button = (By.CSS_SELECTOR, "#root > div > header > div > a:nth-child(7)")
    first_MB = (By.CSS_SELECTOR, "#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div"
                                 ".MuiGrid-root.css-rfnosa > div:nth-child(2)")
    additional_menu_first_MB = (By.CSS_SELECTOR, "#root > div > div:nth-child(3) > div > div > div:nth-child(1) > div >"
                                                 " div > div > div > div:nth-child(2) > div > div.MuiAccordionSummary-c"
                                                 "ontent.MuiAccordionSummary-contentGutters.css-s2q1rt > button")
    second_button_MB = (By.CSS_SELECTOR, "#description-menu > div > ul > li:nth-child(2)")
    confirm_delete_button_MB = (By.CSS_SELECTOR, "body > div > div.MuiBox-root.css-1xt3qe > div > button:nth-child(1)")
    upload_MB = (By.CSS_SELECTOR, "#root > div.MuiBox-root.css-18cq61h > div:nth-child(3) > div > div > div:nth-child(1"
                                  ") > div > div > div > div.MuiGrid-root.css-rfnosa > div > button > input[type=file]")
