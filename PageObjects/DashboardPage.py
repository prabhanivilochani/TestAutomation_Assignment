from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6'

    def is_dashboard_loaded(self):
        return self.driver.find_element(By.XPATH, self.dashboard_header_xpath).is_displayed()