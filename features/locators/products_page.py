from selenium.webdriver.common.by import By

class ProductsPageLocators:
    PAGE_TITLE = (By.CLASS_NAME, "app_logo")
    BURGER_MENU_ICON = (By.CSS_SELECTOR, '[data-test="open-menu"]')
    SHOPPING_CART_ICON = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    SHOPPING_CART_COUNTER = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    INVENTORY_LIST = (By.CSS_SELECTOR, '[data-test="inventory-list"]')

    FILTER_DROPDOWN_MENU = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    FILTER_AZ_OPTION = (By.CSS_SELECTOR, '[value="az"]')
    FILTER_ZA_OPTION = (By.CSS_SELECTOR, '[value="za"]')
    FILTER_LOW_HIGH_OPTION = (By.CSS_SELECTOR, '[value="lohi"]')
    FILTER_HIGH_LOW_OPTION = (By.CSS_SELECTOR, '[value="hilo"]')
    FILTER_OPTIONS = {
        "Name (A to Z)": FILTER_AZ_OPTION,
        "Name (Z to A)": FILTER_ZA_OPTION,
        "Price (low to high)": FILTER_LOW_HIGH_OPTION,
        "Price (high to low)": FILTER_HIGH_LOW_OPTION
    }

    #generic locators for all items
    PRODUCT_ITEM = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, '[data-test="inventory-item-desc"]')
    # Locator for "Add to Cart" buttons, matching any element with a 'data-test' attribute starting with 'add-to-cart-'
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[data-test^="add-to-cart-"]')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '[data-test^="remove-"]')
    PRODUCT_IMAGE = (By.CLASS_NAME, "inventory_item_img")
