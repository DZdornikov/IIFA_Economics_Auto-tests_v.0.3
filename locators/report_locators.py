from selenium.webdriver.common.by import By


class ReportLocators:
    first_report_name = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div > div > div > div:nth-child'
                                          '(5) > div > div > div > div > div > div > div > div:nth-child(1) > div > div'
                                          ' > div > p:nth-child(1)')
    export_report_button = (By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div > div > button')
