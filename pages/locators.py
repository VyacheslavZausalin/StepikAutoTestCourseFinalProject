from selenium.webdriver.common.by import By

#
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

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
    BOOK_TITLE = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    INFO_ABOUT_NEW_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")
    INFO_ABOUT_PRICE_OF_NEW_BOOK = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")