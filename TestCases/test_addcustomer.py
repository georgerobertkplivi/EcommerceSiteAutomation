import pytest
from selenium import webdriver
import time
import string
import random


## Page Objects
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomerPage

## Custom utilities
from Utilities.configs import Configs
from Utilities.browsers import Browser
from Utilities.logging import Loggs

class TestAddCustomPage:

    baseURL = Configs.getURL()
    username = Configs.getUseremail()
    password = Configs.getPassword()
    logs = Loggs.loggen()
    browsers = Browser.browsers
    header_title_xpath = "//h1[@class='pull-left']"
    btnSuccessMessage_xpath = "//div[@class='alert alert-success alert-dismissable']"




    def test_addcustomer_003(self,browsers):
        self.driver = browsers
        self.driver.get(self.baseURL)
        self.login = LoginPage(browsers)
        self.logs.info("*****Starting Test Add New Customer 003 *****")
        self.logs.info("**** Login Into Home Page ****")
        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        self.logs.info("**** Go To Add New Page ****")
        time.sleep(5)
        self.addnew = AddCustomerPage(browsers)
        self.addnew.clickCustomerMenu()
        self.addnew.clickCustomerMenuItem()
        self.addnew.clickAddNew()
        time.sleep(3)
        self.email = random_generator() + "@gmail.com"
        self.addnew.setEmail(self.email)
        self.addnew.setPassword("test123")
        self.addnew.setFirstName("George")
        self.addnew.setLasttName("Robert")
        self.addnew.setGender("Male")
        self.addnew.setDob("12/10/2020")
        self.addnew.setCompanyName("George Farms")
        time.sleep(5)
        self.addnew.setCompanyRole("Administrators")
        self.addnew.setManagerOfVendor("Vendor 1")
        self.addnew.setAdminComment("Testing Add New Customer Page...")
        self.addnew.clickSave()



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))