from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from features.locators.products_page import ProductsPageLocators

class CheckoutPage:
    url = "https://www.saucedemo.com/inventory.html"

    def __init__(self, browser):
        self.browser = browser