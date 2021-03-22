from Utilities.logging import Loggs
from selenium.webdriver.common.by import By
class LoginPage:
    # Login Page Locators
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout"


    #Initialize Class Objects
    logs = Loggs.loggen()

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        browser = self.driver
        browser.find_element(By.ID, self.textbox_username_id).clear()
        browser.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        browser = self.driver
        browser.find_element(By.ID, self.textbox_password_id).clear()
        browser.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        browser = self.driver
        browser.find_element(By.XPATH, self.button_login_xpath).click()


    def clickLogout(self):
        browser = self.driver
        browser.find_element(By.LINK_TEXT, self.link_logout_linktext).click()


