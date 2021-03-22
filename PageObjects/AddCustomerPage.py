import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomerPage:
    # Add customer Page Locators
    # lnkCustomers_menu_xpath = "//a[@h    ref='#']//span[contains(text(),'Customers')]"
    # lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    # btnAddnew_xpath = "//a[@class='btn bg-blue']"
    # txtEmail_xpath = "//input[@id='Email']"
    # txtPassword_xpath = "//input[@id='Password']"
    # txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    # lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    # lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    # lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    # lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    # drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    # rdMaleGender_id = "Gender_Male"
    # rdFeMaleGender_id = "Gender_Female"
    # txtFirstName_xpath = "//input[@id='FirstName']"
    # txtLastName_xpath = "//input[@id='LastName']"
    # txtDob_xpath = "//input[@id='DateOfBirth']"
    # txtCompanyName_xpath = "//input[@id='Company']"
    # txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    # btnSave_xpath = "//button[@name='save']"
    lnkCustomer_menu_xpath = "//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/li[@class='nav-item has-treeview']/a[contains(.,'Customers')]"
    lnkCustomer_menu_item_xpath = "//li[@class='nav-item has-treeview menu-open']/ul[@class='nav nav-treeview']//p[contains(.,'Customers')]"
    btnAddNew_css = "a.btn-primary"
    btnSave_xpath = "//button[@name='save']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    radMaleGender_xpath = "//input[@id='Gender_Male']"
    radFemaleGender_xpath = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    chkTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    txtNewsletter_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']"
    txtCustomerRole_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrator_xpath = "//li[.='Administrators']"
    lstitemGuest_xpath = "//li[.='Guests']"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemVendor_xpath = "//li[.='Vendors']"
    lstitemYourStoreName_xpath = "//div[.='Your store name']"
    drpManagerofVender_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSuccessMessage_xpath = "//div[@class='alert alert-success alert-dismissable']"





    def __init__(self,driver):
        self.driver = driver

    def clickCustomerMenu(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.lnkCustomer_menu_xpath).click()

    def clickCustomerMenuItem(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.lnkCustomer_menu_item_xpath).click()

    def clickAddNew(self):
        browser = self.driver
        browser.find_element(By.CSS_SELECTOR,self.btnAddNew_css).click()

    def setEmail(self,email):
        browser = self.driver
        browser.find_element(By.XPATH,self.txtEmail_xpath).clear()
        browser.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        browser = self.driver
        browser.find_element(By.XPATH, self.txtPassword_xpath).clear()
        browser.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        browser = self.driver
        browser.find_element(By.XPATH, self.txtFirstName_xpath).clear()
        browser.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLasttName(self,lname):
        browser = self.driver
        browser.find_element(By.XPATH, self.txtLastName_xpath).clear()
        browser.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self,gender):
        browser = self.driver
        if gender == 'Male':
            browser.find_element(By.XPATH, self.radMaleGender_xpath).click()
        elif gender == 'Female':
            browser.find_element(By.XPATH, self.radFemaleGender_xpath).click()
        else:
            browser.find_element(By.XPATH, self.radMaleGender_xpath).click()

    def setManagerOfVendor(self,value):
        browser = self.driver
        drp = Select(browser.find_element(By.XPATH,self.drpManagerofVender_xpath))
        drp.select_by_visible_text(value)

    def setDob(self,dob):
        browser = self.driver
        browser.find_element(By.XPATH,self.txtDob_xpath).clear()
        browser.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,companyname):
        browser = self.driver
        browser.find_element(By.XPATH, self.txtCompanyName_xpath).clear()
        browser.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(companyname)



    def setCompanyRole(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRole_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemAdministrator_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
        elif role=='Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendor_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)



    def setAdminComment(self,comments):
        browser = self.driver
        browser.find_element(By.XPATH,self.txtAdminComment_xpath).clear()
        browser.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(comments)

    def clickSave(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.btnSave_xpath).click()












