
from selenium.webdriver.common.by import By



class Login:

    username = "username"
    password = "password"
    loginbtn_Xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'


    def __init__(self, driver):
        self.driver = driver


    def set_Username(self, username):

        self.driver.find_element(By.NAME, self.username).clear()
        self.driver.find_element(By.NAME, self.username).send_keys(username)


    def set_Password(self, password):

        self.driver.find_element(By.NAME, self.password).clear()
        self.driver.find_element(By.NAME, self.password).send_keys(password)


    def click_Login(self):

        self.driver.find_element(By.XPATH, self.loginbtn_Xpath).click()
