from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import  ProductpageLocators
import time

class BasketPage(BasePage):
    def is_product_in_basket(self):
        pass