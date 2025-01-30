from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from features.locators.products_page import ProductsPageLocators

class ProductsPage:
    url = "https://www.saucedemo.com/inventory.html"

    def __init__(self, browser):
        self.browser = browser

    def is_element_visible(self, locator):
        try:
            element = self.browser.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def get_add_to_cart_locator(self, product_name):
        """
        Returns a locator for the "Add to Cart" button of a specific product.
        :param product_name: Unique identifier of the product (e.g., 'sauce-labs-backpack').
        :return: Tuple locator for the specific button.
        """
        return By.CSS_SELECTOR, f'[data-test="add-to-cart-{product_name}"]'

    def click_add_to_cart(self, product_name):
        """
        Clicks the "Add to Cart" button for a specific product.
        :param product_name: Unique identifier of the product.
        """
        add_to_cart_locator = self.get_add_to_cart_locator(product_name)
        button = self.browser.find_element(*add_to_cart_locator)
        button.click()

    def get_remove_from_cart_locator(self, product_name):
        """
        Returns a locator for the "Remove" button of a specific product.
        :param product_name: Unique identifier of the product (e.g., 'sauce-labs-backpack').
        :return: Tuple locator for the specific button.
        """
        return By.CSS_SELECTOR, f'[data-test="remove-{product_name}"]'

    def click_remove_from_cart(self, product_name):
        """
        Clicks the "Add to Cart" button for a specific product.
        :param product_name: Unique identifier of the product.
        """
        remove_from_cart_locator = self.get_remove_from_cart_locator(product_name)
        button = self.browser.find_element(*remove_from_cart_locator)
        button.click()

    def get_shopping_cart_counter_value(self):
        """
        Gets the numeric value displayed in the shopping cart badge.
        :return: Integer value of the cart counter.
        """
        counter_element = self.browser.find_element(*ProductsPageLocators.SHOPPING_CART_COUNTER)
        return int(counter_element.text)

    def select_filter_option(self, filter_name):
        self.browser.find_element(*ProductsPageLocators.FILTER_DROPDOWN_MENU).click()
        option_locator = ProductsPageLocators.FILTER_OPTIONS.get(filter_name)
        self.browser.find_element(*option_locator).click()

    def get_product_names(self):
        # Get all the product names as a list of strings
        product_elements = self.browser.find_elements(*ProductsPageLocators.PRODUCT_TITLE)
        return [product.text for product in product_elements]

    def are_products_sorted_ascending(self):
        product_names = self.get_product_names()
        return product_names == sorted(product_names)

    def are_products_sorted_descending(self):
        product_names = self.get_product_names()
        return product_names == sorted(product_names, reverse=True)

    def get_product_prices(self):
        # Get all the product names as a list of strings
        product_elements = self.browser.find_elements(*ProductsPageLocators.PRODUCT_PRICE)
        return [product.text for product in product_elements]

    def get_numeric_prices(self):
        # Convert price strings to numeric values
        prices = self.get_product_prices()
        return [float(price.replace('$', '')) for price in prices]

    def are_product_prices_sorted_ascending(self):
        product_prices = self.get_numeric_prices()
        return product_prices == sorted(product_prices)

    def are_product_prices_sorted_descending(self):
        product_prices = self.get_numeric_prices()
        return product_prices == sorted(product_prices, reverse=True)