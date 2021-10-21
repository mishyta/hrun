import allure
from pages.basepage import Webdriverhandler
from pages.loginpage import LoginPage
from pages.mainpage import *


@allure.story('test_login_with_valid_creditionals')
def test_login_with_valid_creeds(driver):
    Webdriverhandler(driver)
    page = LoginPage()
    page = page.login_with_valid_creds()


@allure.story('test_login_with_valid_creditionals')
def test_login_with_invalid_creeds(driver):
    Webdriverhandler(driver)
    page = LoginPage()
    page = page.login_with_invalid_creds()


@allure.story('test_login_with_valid_creditionals')
def test_logout(driver):
    Webdriverhandler(driver)
    page = LoginPage()
    page = page.login_with_valid_creds()
    page = page.sb.log_out()
    

@allure.story('Test:Request a new medication')
def test_request_a_new_medication(driver):
    Webdriverhandler(driver)
    with allure.step('Login'):
        page = LoginPage()
        page = page.login_with_valid_creds()    
    with allure.step('Go to Medication:New request page'):
        page.sb.click_option(*SideBar.SUB_NEW_REQUEST)
        page = Medication_NewRequestPage()
    page.sb.assert_primary_contains_sub_items(('Requests', 'Completed', 'New Request', 'Return Medication'))
    page.get_script() # i use this because website is broken
    with allure.step('Fill all fields using next data (Field name: field data):'):
        page.input_patient('test patient','Test - Patient - P00201')
        page.seleect_any_available_date_in_visit()
        page.input_medication('Pramoxine')
        page.input_prescription('Testing prescription')
        page.choose_yesterday_in_prescription_date()
        page.input_quantity_requested(random.randint(1,5))
        page.input_refills(random.randint(5,10))
        page.add_req()
        page.check_med_req_saved_popup()
        page.click_poppup_ok()
    page.check_page_loaded()