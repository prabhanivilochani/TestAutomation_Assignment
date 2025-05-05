from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class HeaderComponent:
    def __init__(self, driver):
        self.driver = driver
        self.profile_menu_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span'
        self.logout_link_text = 'Logout'

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.profile_menu_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, self.logout_link_text).click()
