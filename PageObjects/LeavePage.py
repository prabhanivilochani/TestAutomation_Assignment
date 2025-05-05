from selenium.webdriver.common.by import By

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.my_leave_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[5]/button"
        self.leave_header_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6'

    def click_my_leave(self):
        self.driver.find_element(By.XPATH, self.my_leave_xpath).click()

    def is_leave_page_loaded(self):
        return self.driver.find_element(By.XPATH, self.leave_header_xpath).is_displayed()
