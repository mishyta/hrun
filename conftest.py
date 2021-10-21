import logging
import pytest
from selenium import webdriver
from utils.listener import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from allure_commons.types import AttachmentType
import allure

SELENOID_IP = '10.8.0.46'
SELENOID_HUB_PORT = '4444'
SELENOID_UI_PORT = '8080'
 
BROWSERS_FOR_TESTS = ["chrome", "firefox", "opera"] # ["chrome", "firefox", "opera"]
LOGGING_FILE = 'webdriver.log'
COMMAND_EXECUTOR = "http://{}:{}/wd/hub".format(SELENOID_IP,SELENOID_HUB_PORT)
ALLURE_RESULTS_DIR = 'allure-results'
SELENOID_OPTIONS = {
    "enableVNC": True,
    "enableVideo": False
}

CAPABILITIES_FF = {
    "browserName": "firefox",
    "browserVersion": "92.0",
    "selenoid:options": SELENOID_OPTIONS
}

CAPABILITIES_CHROME = {
    "browserName": "chrome",
    "browserVersion": "93.0",
    "selenoid:options": SELENOID_OPTIONS
}

CAPABILITIES_OPERA = {
    "browserName": "opera",
    "browserVersion": "79.0",
    "selenoid:options": SELENOID_OPTIONS
}

logging.basicConfig(
    filename=LOGGING_FILE,
    level=logging.INFO,
    format='[%(levelname)s][%(asctime)s]:%(message)s'
)


def pytest_configure(config):
    open(LOGGING_FILE, 'w').close()
    config.option.allure_report_dir = ALLURE_RESULTS_DIR
    config.option.clean_alluredir = False


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=BROWSERS_FOR_TESTS)  # Driver fixture
def driver(request):
    if request.param == "chrome":
        capabilities = CAPABILITIES_CHROME
    elif request.param == "firefox":
        capabilities = CAPABILITIES_FF
    elif request.param == "opera":
        capabilities = CAPABILITIES_OPERA
    else:
        print('{} not supported.'.format(request.param))
    with allure.step(
            'Init with capabilities: {}:{}'.format(capabilities['browserName'], capabilities['browserVersion'])):
        driver = webdriver.Remote(
            command_executor=COMMAND_EXECUTOR, desired_capabilities=capabilities)
        # driver = EventFiringWebDriver(driver, MyListener())
        driver.implicitly_wait(10)
        driver.maximize_window()
    yield driver
    with allure.step('Driver teardown.'):
        if request.node.rep_call.failed:
            allure.attach(driver.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)
            allure.attach('http://{}:{}/video/{}.mp4'.format(SELENOID_IP,SELENOID_UI_PORT,driver.session_id), name="Video",
                          attachment_type=allure.attachment_type.MP4)
        driver.quit()

# @pytest.fixture
# def driver():
#     driver = webdriver.Firefox()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

# @pytest.fixture(params=BROWSERS_FOR_TESTS)  # Driver fixture
# def driver(request):
#     if request.param == "chrome":
#         capabilities = CAPABILITIES_CHROME
#     elif request.param == "firefox":
#         capabilities = CAPABILITIES_FF
#     elif request.param == "opera":
#         capabilities = CAPABILITIES_OPERA
#     else:
#         print('{} not supported.'.format(request.param))
#     driver = webdriver.Remote(
#             command_executor=COMMAND_EXECUTOR, desired_capabilities=capabilities)
#     # driver = EventFiringWebDriver(driver, MyListener())
#     driver.implicitly_wait(10)
#     # driver.maximize_window()
#     yield driver
#     driver.quit