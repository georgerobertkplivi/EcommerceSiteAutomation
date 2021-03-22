from Utilities.browsers import Browser
from Utilities.configs import Configs
from Utilities.logging import Loggs
from PageObjects.LoginPage import LoginPage
import time
import pytest

class TestLoginPage:

    baseURL = Configs.getURL()
    username = Configs.getUseremail()
    password = Configs.getPassword()
    logs = Loggs.loggen()
    browsers = Browser.browsers

    def test_homePageTitle_001(self,browsers):
        self.driver = browsers
        self.login = LoginPage(browsers)
        self.logs.info("*************** Test_homePageTitle_001 *****************")
        self.logs.info("****Started Home page title test ****")
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_page_title = self.driver.title
        if act_page_title == "Your store. Login":
            self.logs.info("***** Home Page Title Test Passed *****")
            assert True
        else:
            self.driver.error("***** Home Page Title Page Test Failed *****")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_homepagetitle.png")
            assert False
        self.logs.info("************* Login Successful *************")
        self.logs.info("********** Test Home Page Title **********")
        time.sleep(4)
        self.logs.info("***** Home Page Title Test Successful *****")



    def test_homePageLogin_002(self,browsers):
        self.driver = browsers
        self.login = LoginPage(browsers)
        self.logs.info("*************** Test_homePageLogin_002 *****************")
        self.logs.info("****Started Home page title test ****")
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        self.logs.info("************* Login Successful *************")
        self.logs.info("********** Test Home Page Title **********")
        time.sleep(4)
        act_page_title = self.driver.title
        if act_page_title == "Dashboard / nopCommerce administration":
            self.logs.info("***** Dashboard Page Title Test Passed -- Your on the Dashboard *****")
            assert True
        else:
            self.driver.error("***** Home Page Title Page Test Failed *****")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_dashboardpagetitle.png")
            assert False
        #assert "Dashboard / nopCommerce administration" in act_page_title
        time.sleep(4)
        self.login.clickLogout()
        self.logs.info("************* Login Test Successful *************")


