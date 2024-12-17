from selenium.webdriver.common.by import By


class ShoppingCartPageLocators:
    SHOPPING_CART_ICON = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    SHOPPING_CART_COUNTER = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    BURGER_MENU_ICON = (By.CSS_SELECTOR, '[data-test="open-menu"]')
    CART_LIST = (By.CSS_SELECTOR, '[data-test="cart-list"]')

    PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, '[data-test="inventory-item-desc"]')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, '[data-test="item-quantity"]')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '[data-test^="remove-"]')

    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, '[data-test="continue-shopping"]')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="checkout"]')

