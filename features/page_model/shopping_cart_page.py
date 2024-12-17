from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class ShoppingCartPage:
    url = "https://www.saucedemo.com/cart.html"

    def __init__(self, browser):
        self.browser = browser

    def is_element_visible(self, locator):
        try:
            element = self.browser.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def get_item_locator(self, product_title):
        """
        Returns a locator for the "Add to Cart" button of a specific product.
        :param product_name: Unique identifier of the product (e.g., 'sauce-labs-backpack').
        :return: Tuple locator for the specific button.
        """
        return By.XPATH, f'//div[@class="cart_item"]//*[contains(text(), "{product_title}")]'


