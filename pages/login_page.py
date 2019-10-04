import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password input is not presented"        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email input is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration password-1 input is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration password-2 input is not presented"

    def register_new_user(self, email, password):        
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
