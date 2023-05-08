from selenium.webdriver.common.by import By

#
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    EMAIL_LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-password")
    EMAIL_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductpageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
