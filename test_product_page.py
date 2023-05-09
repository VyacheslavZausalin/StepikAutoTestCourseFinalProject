from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    #time.sleep(2)
    page.add_product_to_basket()
    time.sleep(2)
    page.is_product_in_basket()
    time.sleep(2)
    page.price_of_book_added_to_basket()
    time.sleep(30)