from Page.BasePage import BasePage
from Locator.LoginLocator import LoginLocator
from Data.LoginData import LoginData


class LoginPage(BasePage):

    """Locator for Login Page"""
    username_textbox = LoginLocator.username_textbox
    password_textbox = LoginLocator.password_textbox
    login_button = LoginLocator.login_button
    # invalid_username_messageText = LoginLocator.invalid_username_messageText
    """Test Data for Login Page"""
    valid_username = LoginData.valid_username
    invalid_username = LoginData.invalid_username
    valid_password = LoginData.valid_password
    invalid_password = LoginData.invalid_password

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for Login Page"""

    def get_login_page_title(self, title):
        return self.getTitle(title)

    def enter_valid_username(self):
        self.sendText(self.username_textbox, self.valid_username)

    def enter_invalid_username(self):
        self.sendText(self.username_textbox, self.invalid_username)

    def enter_valid_password(self):
        self.sendText(self.password_textbox, self.valid_password)

    def enter_invalid_password(self):
        self.sendText(self.password_textbox, self.invalid_password)

    def click_login_button(self):
        self.click_on(self.login_button)

    def get_invalid_username_messageText(self):
        actual_message = self.getText(self.invalid_username_messageText)
        return actual_message
