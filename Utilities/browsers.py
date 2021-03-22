import pytest
from selenium import webdriver
from Utilities.configs import Configs

global url
url = Configs.getURL()

class Browser:

    @pytest.fixture()
    def browsers(self):
        driver = webdriver.Chrome(executable_path="C:/Users/mm195/Desktop/YMLILGEE/Programs/Gecko Driver/chromedriver_win32/chromedriver.exe")
       # driver.get(url)
        driver.implicitly_wait(15)
        # Return the driver object at the end of setup
        yield driver

        # For cleanup, quit the driver
        driver.quit()