
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
import pages.loginpage
from pages.mainpage import *

class SideBar(BasePage):   

    CURRENT_PAGE_TITLE = (By.CSS_SELECTOR, '.view-top-bar')        
    SETTINGS_GEAR = (By.XPATH, '//*[@class="mega-octicon octicon-gear"]')
    LOGOUT = (By.CSS_SELECTOR, 'a.logout')
    SIDE_BAR_SUB_ITEM = (By.CSS_SELECTOR, 'a.category-sub-item')

#           PRIMARY  css_selector = 'div.primary-nav-item  a[href="<from 1st sub item>"]'
#              |-->SUB  css_selector = 'div.category-sub-items  a[href="current item"]'
#              |-->SUB  
#               ...
#              |-->SUB
#
#           EXAPLE:
#           PRIMARY_PATIENTS = (By.CSS_SELECTOR, 'div.primary-nav-item  a[href="#/patients"]')
#              |-->SUB_PATIENT_LISTING = (*PRIMARY_PATIENTS, By.CSS_SELECTOR, 'div.category-sub-items a[href="#/patients"]')
#              |-->SUB_ADMITTED_PATIENTS = (*PRIMARY_PATIENTS, By.CSS_SELECTOR, 'div.category-sub-items a[href="#/patients/admitted"]')
#               ...
#              |-->SUB_REPORTS = (*PRIMARY_PATIENTS, By.CSS_SELECTOR, 'div.category-sub-items a[href="#/patients/reports"]')
#            ...
#   PRIMARY: 
    PRIMARY_PATIENTS = (By.CSS_SELECTOR, 'div.primary-nav-item  a[href="#/patients"]')
    PRIMARY_SCHEDULING = (By.CSS_SELECTOR, 'div.primary-nav-item  a[href="#/appointments"]')
    PRIMARY_MEDICATION = (By.CSS_SELECTOR, 'div.primary-nav-item  a[href="#/medication"]')
#   SUB_ = (*PRIMARY_PATIENTS, By.CSS_SELECTOR, '')    
    SUB_PATIENT_LISTING = (*PRIMARY_PATIENTS, By.CSS_SELECTOR, 'div.category-sub-items a[href="#/patients"]')
    SUB_ADMITTED_PATIENTS = (*PRIMARY_PATIENTS, By.CSS_SELECTOR, 'div.category-sub-items a[href="#/patients/admitted"]')
    SUB_OUTPATIENT = (*PRIMARY_PATIENTS,By.CSS_SELECTOR, 'div.category-sub-items a[href="#/patients/outpatient"]')
    SUB_NEW_PATIENT = (*PRIMARY_PATIENTS, By.CSS_SELECTOR, 'div.category-sub-items a[href="#/patients/edit/new"]')
    SUB_REPORTS = (*PRIMARY_PATIENTS, By.CSS_SELECTOR, 'div.category-sub-items a[href="#/patients/reports"]')  
#   SUB_ = (*PRIMARY_SCHEDULING, By.CSS_SELECTOR, '')       
    SUB_APPOINTMENTS_THIS_WEEK = (*PRIMARY_SCHEDULING ,By.CSS_SELECTOR, 'div.category-sub-items a[href="#/appointments"]')
#   SUB_ = (*PRIMARY_MEDICATION, By.CSS_SELECTOR, '')  
    SUB_NEW_REQUEST = (*PRIMARY_MEDICATION, By.CSS_SELECTOR, 'div.category-sub-items a[href="#/medication/edit/new"]')

    @allure.step('Log out')
    def log_out(self):
        self.click_on_element(*SideBar.SETTINGS_GEAR)
        self.click_on_element(*SideBar.LOGOUT)
        self.check_element_exist(*pages.loginpage.LoginPage.PAGE_LOGO)
        self = pages.loginpage.LoginPage()
    
    @allure.step('Search')
    def search(self):
        pass

    @allure.step('Check that primary item was not opened')    
    def check_primary_item_opened(self,primary_find_by, primary_locator) -> bool:
        elem = self.get_element(primary_find_by,primary_locator)
        if len(elem.find_elements(By.XPATH, "./../../div")) >1:
            return True
            

    @allure.step('Select sidebar otipon')
    def click_option(self, primary_find_by, primary_locator, sub_find_by, sub_locator):
        if not self.check_primary_item_opened(primary_find_by, primary_locator):
            self.click_on_element(primary_find_by, primary_locator)
        self.click_on_element(sub_find_by, sub_locator)

    @allure.step('Get all sub_item names from opened primary')    
    def get_sub_items_names_from_active_primery_item(self) -> tuple:
        elements = self.get_elements(*SideBar.SIDE_BAR_SUB_ITEM)
        return tuple(element.text for element in elements)

    @allure.step('Assert that primary cpntains sub items')
    def assert_primary_contains_sub_items(self,items:tuple):        
        assert set(items).issubset(self.get_sub_items_names_from_active_primery_item())      
