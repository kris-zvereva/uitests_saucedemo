from features.locators.products_page import ProductsPageLocators

class ProductsPage:
    url = "https://www.saucedemo.com/inventory.html"

    def __init__(self, browser):
        self.browser = browser

    def is_element_visible(self, locator):
        return self.browser.find_element(*locator).is_displayed()