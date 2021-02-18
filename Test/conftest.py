import sys
sys.path.append('/Users/silviaho/Documents/tc-studio-qa/')
# import os
# sys.path.append(os.environ['WORKSPACE'])
import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utility.ReadConfig import ReadConfig


@pytest.fixture(params=["chrome","firefox"], scope="function")
# @pytest.fixture(params=["chrome", "firefox", "safari"], scope="function")
def init_driver(request):
    global driver
    base_URL = ReadConfig.getBase_URL()
    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install(), service_log_path='/dev/null')
    elif request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), service_log_path='/dev/null')
    elif request.param == "safari":
        driver = webdriver.Safari()
    else:
        print("Your browser name: " + request.param + " is incorrect")
        raise Exception("driver is undefined")
    request.cls.driver = driver
    driver.delete_all_cookies()
    driver.maximize_window()
    if isinstance(base_URL, str):
        driver.get(base_URL)
    else:
        driver.quit()
        raise TypeError("URL must be a string")
    yield
    if AssertionError:
        allure.attach(driver.get_screenshot_as_png(),
                      name="Invalid or Failed Test Cases",
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture(params=["chrome_headless", "firefox_headless"], scope="function")
# @pytest.fixture(params=["chrome_headless", "firefox_headless", "safari_headless"], scope="function")
def init_driver_headless(request):
    global driver
    base_URL = ReadConfig.getBase_URL()
    if request.param == "chrome_headless":
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, service_log_path='/dev/null')
    elif request.param == "firefox_headless":
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options,
                                   service_log_path='/dev/null')
    elif request.param == "safari":
        driver = webdriver.Safari()
    else:
        print("Your browser name: " + request.param + " is incorrect")
        raise Exception("driver is undefined")
    request.cls.driver = driver
    driver.delete_all_cookies()
    driver.maximize_window()
    if isinstance(base_URL, str):
        driver.get(base_URL)
    else:
        driver.quit()
        raise TypeError("URL must be a string")
    yield
    if AssertionError:
        allure.attach(driver.get_screenshot_as_png(),
                      name="Invalid or Failed Test Cases",
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture(params=["chrome_incognito", "firefox_incognito"], scope="function")
# @pytest.fixture(params=["chrome_incognito", "firefox_incognito", "safari_incognito"], scope="function")
def init_driver_incognito(request):
    global driver
    base_URL = ReadConfig.getBase_URL()
    if request.param == "chrome_incognito":
        options = webdriver.ChromeOptions()
        options.add_argument("incognito")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, service_log_path='/dev/null')
    elif request.param == "firefox_incognito":
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=firefoxProfile,
                                   service_log_path='/dev/null')
    elif request.param == "safari":
        driver = webdriver.Safari()
    else:
        print("Your browser name: " + request.param + " is incorrect")
        raise Exception("driver is undefined")
    request.cls.driver = driver
    driver.delete_all_cookies()
    driver.maximize_window()
    if isinstance(base_URL, str):
        driver.get(base_URL)
    else:
        driver.quit()
        raise TypeError("URL must be a string")
    yield
    if AssertionError:
        allure.attach(driver.get_screenshot_as_png(),
                      name="Invalid or Failed Test Cases",
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()
