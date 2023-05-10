# импорт базового класса BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
# создаём` класс  MainPage. Его нужно сделать наследником класса BasePage
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)