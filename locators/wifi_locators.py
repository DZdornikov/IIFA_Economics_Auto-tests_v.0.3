from selenium.webdriver.common.by import By


class WifiLocators:

    click_on_username = (By.XPATH, "//*[@id='app']/div/div/form/div[1]/div/div/input")

    click_on_password = (By.XPATH, "//*[@id='app']/div/div/form/div[2]/div/div/input")

    sign_in_button = (By.XPATH, "//*[@id='app']/div/div/button")

    click_on_devices = (By.XPATH, "//*[@id='app']/div/section/section/aside/div/ul[1]/li[4]/div/img")

    click_on_list_button = (By.XPATH, "//*[@id='scroll-view']/div[2]/div[1]/div[2]/div[2]/div[2]")

    click_on_restart_button = (By.XPATH, "//*[@id='scroll-view']/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[8]/di"
                                         "v/button[2]")