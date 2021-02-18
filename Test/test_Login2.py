# import sys
# sys.path.append('/Users/silviaho/Documents/tc-studio-qa/')
# import os
# sys.path.append(os.environ['WORKSPACE'])
from Page.LoginPage import LoginPage
from Page.DashboardPage import DashboardPage
import pytest
import allure
import time

# Any test file, class and method name should start with "test_" for pytest to run
# -v stands for more info metadata; -s logs in output;
# -k stands for specific method names execution; -n means how many browsers running
# -m means running pytest with mark(tag), ex: @pytest.mark.smoke
# -h to see what pytest commands are available
# To skip a test: @pytest.mark.skip
# To skip a test without reporting pass or fail but still run the test: @pytest.mark.xfail


@pytest.mark.usefixtures("init_driver")
class Test_Login_Two():
    @allure.description("Validates login page with valid login credentials")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.smoke
    def test_validLogin_two(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_valid_username()
        self.loginPage.enter_valid_password()
        self.loginPage.click_login_button()
        self.dashboardPage = DashboardPage(self.driver)
        assert self.dashboardPage.is_signOut_link_visible()

    @allure.description("Validates login page with invalid login credentials")
    @allure.severity(severity_level="NORMAL")
    def test_invalidLogin_two(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_invalid_username()
        self.loginPage.enter_invalid_password()
        self.loginPage.click_login_button()
        self.dashboardPage = DashboardPage(self.driver)
        try:
            assert self.dashboardPage.is_signOut_link_visible()
        finally:
            if AssertionError:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="Invalid Credentials",
                              attachment_type=allure.attachment_type.PNG)

    # @allure.description("Validates OrangeHRM with valid login credentials")
    # @allure.severity(severity_level="CRITICAL")
    # @pytest.mark.parametrize("username, password", [("sylvia@tunecore.com", "Test@123")])
    # def test_validLogin_para(self, username, password):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.enter_valid_username()
    #     self.loginPage.enter_valid_password()
    #     self.loginPage.click_login_button()
    #     self.dashboardPage = DashboardPage(self.driver)
    #     assert self.dashboardPage.is_signOut_link_visible()
    #
    # @allure.description("Validates OrangeHRM with invalid login credentials")
    # @allure.severity(severity_level="NORMAL")
    # @pytest.mark.parametrize("username, password", [("sylvia@tunecore.co", "Test@12")])
    # def test_invalidLogin_para(self, username, password):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.enter_invalid_username()
    #     self.loginPage.enter_invalid_password()
    #     self.loginPage.click_login_button()
    #     self.dashboardPage = DashboardPage(self.driver)
    #     try:
    #         assert self.dashboardPage.is_signOut_link_visible()
    #     finally:
    #         if AssertionError:
    #             allure.attach(self.driver.get_screenshot_as_png(),
    #                           name="Invalid Credentials",
    #                           attachment_type=allure.attachment_type.PNG)
