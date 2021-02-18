from selenium.webdriver.common.by import By


class LoginLocator:

    # LoginPage Objects
    username_textbox = (By.ID, "email")
    password_textbox = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "span.tcstudio-MuiButton-label")
    # invalid_username_messageText = (By.CSS_SELECTOR, "span#spanMessage")
