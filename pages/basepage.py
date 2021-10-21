from selenium.common.exceptions import NoSuchElementException 
import allure
from selenium.webdriver.common.action_chains import ActionChains

class Webdriverhandler():

    driver = None

    def __init__(self, driver) -> None:
        Webdriverhandler.driver = driver

    def get_driver() -> driver:
        return Webdriverhandler.driver

class BasePage():

    def __init__(self) -> None:
        self.driver = Webdriverhandler.get_driver()
        
    def get_url(self):
        with allure.step('Get current url:"{}"'.format(self.driver.current_url)):
            return self.driver.current_url

    def open_page(self, url):
        with allure.step('Open page:"{}"'.format(url)):
            self.driver.get(url)

    def get_element(self, find_by, find_by_value):
        with allure.step('Get element:{}="{}"'.format(find_by, find_by_value)):
            return self.driver.find_element(find_by, find_by_value)
    
    def get_elements(self, find_by, find_by_value):
        with allure.step('Get elements:{}="{}"'.format(find_by, find_by_value)):
            return self.driver.find_elements(find_by, find_by_value)

    def get_element_text(self, find_by, find_by_value):
        with allure.step('Get text from element:{}="{}"'.format(find_by, find_by_value)):
            return self.driver.find_element(find_by, find_by_value).text

    def write_to_element(self, find_by, find_by_value, value: str):
        with allure.step('Type "{}" in element with {}="{}"'.format(value, find_by, find_by_value)):
            self.driver.find_element(find_by, find_by_value).send_keys(value)

    def write_to_element_by_action(self,find_by, find_by_value, value: str):
        with allure.step('Type "{}" to element use action:{}="{}"'.format(value,find_by, find_by_value)):
            element = self.get_element(find_by, find_by_value)
            action = ActionChains(self.driver)
            action.move_to_element(element).click()
            # for char in value:
            #     action.key_down(char).key_up(char)
            action.send_keys(value)
            action.perform()

    def click_on_element(self, find_by, find_by_value):
        with allure.step('Click on element with {}="{}"'.format(find_by, find_by_value)):
            self.driver.find_element(find_by, find_by_value).click()

    def click_on_element_by_action(self,find_by, find_by_value ):
        with allure.step('Click on element with {}="{}" by action'.format(find_by, find_by_value)):    
            element = self.get_element(find_by, find_by_value)
            ActionChains(self.driver).move_to_element(element).click()


    def check_element_exist(self, find_by, find_by_value):
        with allure.step('Check elemnt({}="{}") exist'.format(find_by, find_by_value)): 
            try:
                self.driver.find_element(find_by,find_by_value)
            except NoSuchElementException:
                return False
            return True

    