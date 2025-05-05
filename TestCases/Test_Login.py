# Tests/test_Login.py
from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage
from PageObjects.HeaderComponent import HeaderComponent
import time

class Test_OrangeHRM:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(3)

    def teardown(self):
        self.driver.quit()

    def test_LoginpageTitle(self):
        self.setup()
        assert self.driver.title == "OrangeHRM"
        self.teardown()

    def test_login(self):
        self.setup()
        lp = Login(self.driver)
        lp.set_Username(self.username)
        lp.set_Password(self.password)
        lp.click_Login()
        time.sleep(3)
        dashboard = DashboardPage(self.driver)
        assert dashboard.is_dashboard_loaded()
        self.teardown()

    def test_my_leave_navigation(self):
        self.setup()
        lp = Login(self.driver)
        lp.set_Username(self.username)
        lp.set_Password(self.password)
        lp.click_Login()
        time.sleep(3)
        leave = LeavePage(self.driver)
        leave.click_my_leave()
        time.sleep(3)
        assert leave.is_leave_page_loaded()
        self.teardown()

    def test_logout(self):
        self.setup()
        lp = Login(self.driver)
        lp.set_Username(self.username)
        lp.set_Password(self.password)
        lp.click_Login()
        time.sleep(3)
        header = HeaderComponent(self.driver)
        header.click_logout()
        time.sleep(3)
        assert "login" in self.driver.current_url.lower()
        self.teardown()
