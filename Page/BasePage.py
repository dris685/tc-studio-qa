from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages"""
"""It contains all the generic methods and utilities for all pages"""


class BasePage:

    def __init__(self, driver):
        wait_time_out = 5
        self.driver = driver
        self.webDriverWait = WebDriverWait(self.driver, wait_time_out)

    def getTitle(self, title):
        self.webDriverWait.until(EC.title_is(title))
        return self.driver.title

    def isURLValid(self, URLText):
        isURLValid = self.webDriverWait.until(EC.url_to_be(URLText))
        return isURLValid

    def sendText(self, locator, text):
        self.webDriverWait.until(EC.presence_of_element_located(locator)).clear()
        self.webDriverWait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def click_on(self, locator):
        self.webDriverWait.until(EC.element_to_be_clickable(locator)).click()

    def getText(self, locator):
        actual_text = self.webDriverWait.until(EC.presence_of_element_located(locator)).text
        return actual_text

    def isVisible(self, locator):
        isVisible = self.webDriverWait.until(EC.visibility_of_element_located(locator))
        return isVisible

    def isEnabled(self, locator):
        isEnabled = self.webDriverWait.until(EC.visibility_of_element_located(locator)).is_enabled()
        return isEnabled

    def isSelected(self, locator):
        isSelected = self.webDriverWait.until(EC.visibility_of_element_located(locator)).is_selected()
        return isSelected

    def isDisplayed(self, locator):
        isDisplayed = self.webDriverWait.until(EC.element_located_to_be_selected(locator)).is_displayed()
        return isDisplayed


