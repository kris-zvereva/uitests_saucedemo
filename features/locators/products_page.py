from selenium.webdriver.common.by import By

class ProductsPageLocators:
    PAGE_TITLE = (By.CLASS_NAME, "app_logo")
    BURGER_MENU_ICON = (By.CSS_SELECTOR, '[data-test="open-menu"]')
    SHOPPING_CART_ICON = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    FILTER_DROPDOWN_MENU = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    INVENTORY_LIST = (By.CSS_SELECTOR, '[data-test="inventory-list"]')

    #generic locators for all items
    PRODUCT_ITEM = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, '[data-test="inventory-item-desc"]')
    # Locator for "Add to Cart" buttons, matching any element with a 'data-test' attribute starting with 'add-to-cart-'
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[data-test^="add-to-cart-"]')
    PRODUCT_IMAGE = (By.CLASS_NAME, "inventory_item_img")