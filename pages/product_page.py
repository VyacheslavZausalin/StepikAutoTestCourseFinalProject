from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import  ProductpageLocators
import time
class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductpageLocators.ADD_TO_BASKET_BUTTON)
        add_product.click()
        self.solve_quiz_and_get_code()
        time.sleep(2)

    #def solve_quiz(self):


    def is_product_in_basket(self):
        pass