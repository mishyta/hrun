
import allure
from selenium.webdriver.common.by import By
from pages.sidebar import SideBar
from pages.basepage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random

class MainPage(BasePage):

    

    CURRENT_PAGE_TITLE = (By.CSS_SELECTOR, '.view-current-title')
    PAGE_TITTLE_TEXT = None

    def get_tittle_text(self):
        return self.driver.find_element(*self.CURRENT_PAGE_TITLE).text

    def __init__(self) -> None:
        super().__init__()
        self.sb = SideBar()
        self.check_page_loaded()

    def check_page_loaded(self):
        with allure.step('{} page loaded'.format(self.get_tittle_text())):
            assert self.check_element_exist(*self.CURRENT_PAGE_TITLE) 
        # assert self.get_element(*self.CURRENT_PAGE_TITLE).text == self.PAGE_TITTLE_TEXT 
    
        
# classname = <primary_item>_<sub_item>Page

class Patients_PatientListingPage(MainPage):
    PAGE_TITTLE_TEXT = 'Patient Listing'
    pass
           
class Patients_AdmittedPatientsPage(MainPage):
    pass

class Patients_OutpatientPage(MainPage):
    pass

class Patients_NewPatientPage(MainPage):
    pass

class Patients_ReportsPage(MainPage):
    pass

class Scheduling_AppointmentsThisWeekPage(MainPage):
    pass

class Scheduling_TodaysAppointmentsPage(MainPage):
    pass

class Scheduling_AppointmentSearchPage(MainPage):
    pass

class Scheduling_AppointmentsCalendarPage(MainPage):
    pass

class Scheduling_AddAppointmentPage(MainPage):
    pass

class Scheduling_TheaterSchedulePage(MainPage):
    pass

class Scheduling_ScheduleSurgeryPage(MainPage):
    pass

class Imaging_RequestsPage(MainPage):
    pass

class Imaging_CompletedPage(MainPage):
    pass

class Medication_RequestsPage(MainPage):
    PAGE_TITTLE_TEXT = 'Medication Requests'
    pass

class Medication_CompletedPage(MainPage):
    pass

class Medication_NewRequestPage(MainPage):


    PAGE_TITTLE_TEXT = 'New Medication Request'
    
    PATIENT_FIELD = (By.XPATH, '//*[text()="Patient"]/../div')
    MEDICATION_FIELD = (By.XPATH, '//*[text()="Medication"]/../div')
    VISIT_SELECT = (By.XPATH, '//*[text()="Visit"]/../div/select')
    PRESCRIPTION_FIELD = (By.XPATH,'//*[text()="Prescription"]/../div')
    PRESCRIPTION_DATE_SELECT = (By.XPATH, '//*[text()="Prescription Date"]/../div')
    QUANTITY_REQUESTED_FIELD = (By.XPATH, '//*[text()="Quantity Requested"]/../div/input')
    REFILLS_FIELD = (By.XPATH, '//*[text()="Refills"]/../div/input')
    ADD_BTN = (By.XPATH, '//button[text()="Add"]')
    
    # Medication Request Saved popup locators
    POPUP = (By.CSS_SELECTOR , 'div.modal-dialog')
    POPUP_TITTLE = (By.CSS_SELECTOR, 'div.modal-header .modal-title')
    POPUP_MASSEGE = (By.CSS_SELECTOR, 'div.modal-body')
    POPUP_CROSS_BTN = (By.CSS_SELECTOR, 'button.close')
    POPUP_OK_BTN = (By.CSS_SELECTOR, '.modal-footer .btn')
    
    @allure.step('check script(antipatern)')
    def get_script(self):
        self.driver.implicitly_wait(0)
        l = list()
        while True:    
            if not len(l)>0:
                self.write_to_element_by_action(*Medication_NewRequestPage.PATIENT_FIELD,'t')
                l = list(self.get_elements(By.CSS_SELECTOR,'.tt-suggestion'))
                self.write_to_element_by_action(*Medication_NewRequestPage.PATIENT_FIELD,Keys.BACKSPACE)
            else:
                break
        self.driver.implicitly_wait(3)    

    @allure.step('Patiend: Test Patient (after typing patient name, select “Test Patient - P00201” from dropdown of the same patients')
    def input_patient(self,value,select): # work only with Patient
        self.write_to_element_by_action(*Medication_NewRequestPage.PATIENT_FIELD ,value)
        self.click_on_element(By.XPATH, "//*[text()='{}']".format(select))        

    @allure.step('Medication: Pramoxine (after typing, select any from dropdown of available medication)')
    def input_medication(self,value):
        self.write_to_element_by_action(*Medication_NewRequestPage.MEDICATION_FIELD ,value)
        self.click_on_element(By.XPATH, "//*[contains(@class, 'tt-highlight')][contains(text(),'{}')]".format(value))

    @allure.step('Visit: click on field and select any available date')    
    def seleect_any_available_date_in_visit(self):
        while True:       # checks the select is loaded
            select = Select(self.get_element(*Medication_NewRequestPage.VISIT_SELECT))
            if len(select.options) >1: # if loaded, select random option
                select.select_by_index(random.randint(2,len(select.options)-1))
                break

    @allure.step('Prescription: Testing prescription')            
    def input_prescription(self,value):
        self.write_to_element_by_action(*Medication_NewRequestPage.PRESCRIPTION_FIELD,value)

    @allure.step('Prescription Date: use date of 1 day before, from current date')
    def choose_yesterday_in_prescription_date(self):
        self.click_on_element(*Medication_NewRequestPage.PRESCRIPTION_DATE_SELECT)
        action = ActionChains(self.driver)
        action.send_keys(Keys.LEFT + Keys.ENTER)
        action.perform()

    @allure.step('Quantity Requested: type random number')
    def input_quantity_requested(self,value):
        self.write_to_element(*Medication_NewRequestPage.QUANTITY_REQUESTED_FIELD,value)

    @allure.step('Refils: type random number')
    def input_refills(self,value):
        self.write_to_element(*Medication_NewRequestPage.REFILLS_FIELD,value)

    @allure.step('Click Add button')
    def add_req(self):
        self.click_on_element(*Medication_NewRequestPage.ADD_BTN)

    @allure.step('Assert that Medication Request Saved popup is displayed and contains next items: Ok button and Cross button')
    def check_med_req_saved_popup(self):
        assert self.check_element_exist(*Medication_NewRequestPage.POPUP)
        assert self.check_element_exist(*Medication_NewRequestPage.POPUP_CROSS_BTN)
        assert self.check_element_exist(*Medication_NewRequestPage.POPUP_OK_BTN)
    
    @allure.step('Click Ok button')
    def click_poppup_ok(self):
        self.click_on_element_by_action(*Medication_NewRequestPage.POPUP_OK_BTN)

    
class Medication_DispensePage(MainPage):
    pass

class Medication_ReturnMedicationPage(MainPage):
    pass

class Labs_RequestsPage(MainPage):
    pass

class Labs_CompletedPage(MainPage):
    pass

class Labs_NewRequestPage(MainPage):
    pass

class Billing_InvoicesPage(MainPage):
    pass

class Billing_NewInvoicePage(MainPage):
    pass

class Billing_PricesPage(MainPage):
    pass

class Billing_PriceProfilesPage(MainPage):
    pass

class Billing_CashierPage(MainPage):
    pass

class Incident_CurrentIncidentPage(MainPage):
    pass

class Incident_NewIncidentPage(MainPage):
    pass

class Incident_HistoryPage(MainPage):
    pass

class Incident_ReportsPage(MainPage):
    pass

class Administration_AddressFieldsPage(MainPage):
    pass

class Administration_CustomFormsPage(MainPage):
    pass

class Administration_IncidentCategoriesPage(MainPage):
    pass

class Administration_LoadDBPage(MainPage):
    pass

class Administration_LookupListsPage(MainPage):
    pass

class Administration_ShortcodesPage(MainPage):
    pass

class Administration_PrintHeaderPage(MainPage):
    pass

class Administration_UserRolesPage(MainPage):
    pass