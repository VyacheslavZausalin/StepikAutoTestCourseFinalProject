from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url
        assert "login" in login_url, "Некорректный url адрес"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN_FORM) and \
               self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN_FORM),"Нет формы логина"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTRATION_FORM) and \
               self.is_element_present(*LoginPageLocators.PASSWORD1_REGISTRATION_FORM) and \
               self.is_element_present(*LoginPageLocators.PASSWORD2_REGISTRATION_FORM), "Нет формы регистрации"