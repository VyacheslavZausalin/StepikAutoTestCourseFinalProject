from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import  ProductpageLocators
from selenium.common.exceptions import NoAlertPresentException
import time
class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductpageLocators.ADD_TO_BASKET_BUTTON)
        add_product.click()
        time.sleep(1)
        self.solve_quiz_and_get_code()
        #time.sleep(2)

    #def solve_quiz(self):


    def is_product_in_basket(self):
        message = self.browser.find_element(*ProductpageLocators.INFO_ABOUT_NEW_BOOK_IN_BASKET).text
        book_name = self.browser.find_element(*ProductpageLocators.BOOK_TITLE).text
        assert book_name == message\
               , "There's no book's selected in basket!!"
        print(book_name)
        print(message)

    def price_of_book_added_to_basket(self):
        info_price = self.browser.find_element(*ProductpageLocators.INFO_ABOUT_PRICE_OF_NEW_BOOK).text
        product_price = self.browser.find_element(*ProductpageLocators.PRODUCT_PRICE).text
        assert product_price in info_price, "Wrong price!!!!"
        print(f'Price in the info is: {info_price}')
        print(f'Product price is: {product_price}')