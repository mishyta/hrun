
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
import allure
from pages.mainpage import Patients_PatientListingPage
from pages.basepage import BasePage
from utils.rndm import CreedsGenerator as CG
from utils.crds import crds 
class LoginPage(BasePage):  




    URL = 'http://demo.hospitalrun.io/#/login'
    VALID_CREEDS = crds.get()
    INVALID_CREEDS = ('some.mail@exaple.io', CG.generate_pswrd(8))

    # elements locators:
    LOGIN_FIELD = (By.XPATH, '//*[@id="identification"]')
    PSWRD_FIELD = (By.XPATH, '//*[@id="password"]')
    SBMT_BTN = (By.XPATH, '//*[@class="btn btn-lg btn-primary btn-block"]')
    PAGE_LOGO = (By.XPATH, '//*[@class="logo-svg"]')
    FORM_SIGNIN_ALERT = (By.CSS_SELECTOR, 'div.form-signin-alert')



    def input_creds(self,login, password):
        with allure.step('login  {}:<pswrd>'.format(login)):
            self.write_to_element(*LoginPage.LOGIN_FIELD, login)
            self.write_to_element(*LoginPage.PSWRD_FIELD, password)

    def Sign_In(self):
        self.click_on_element(*LoginPage.SBMT_BTN)

    def login_with_valid_creds(self) -> Patients_PatientListingPage :
        self.open_page(LoginPage.URL)
        self.input_creds(*LoginPage.VALID_CREEDS)
        self.Sign_In()
        return Patients_PatientListingPage()


    def login_with_invalid_creds(self) ->  None:
        self.open_page(LoginPage.URL)
        self.input_creds(*LoginPage.INVALID_CREEDS)
        self.Sign_In()
        self.check_element_exist(*LoginPage.FORM_SIGNIN_ALERT)

    