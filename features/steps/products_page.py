from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from features.locators.products_page import ProductsPageLocators
from features.page_model.login_page import LoginPage
from features.page_model.products_page import ProductsPage


use_step_matcher('re')

@given('I am logged in as "(.*)"')
def step_impl(context, username):
    service = Service('/Users/kristinazvereva/chromedriver')
    context.browser = webdriver.Chrome(service=service)
    context.LoginPage = LoginPage(context.browser)
    context.browser.get(LoginPage.url)
    context.LoginPage.enter_username(username)
    context.LoginPage.enter_password("secret_sauce")  #TODO: do not keep it here
    context.LoginPage.press_login_button()

@given('I am on the products page')
def step_impl(context):
    context.ProductsPage = ProductsPage(context.browser)
    assert context.browser.current_url == "https://www.saucedemo.com/inventory.html"

@then('I see the page title')
def step_impl(context):
    assert context.ProductsPage.is_element_visible(ProductsPageLocators.PAGE_TITLE)

@then('I see the burger menu icon')
def step_impl(context):
    assert context.ProductsPage.is_element_visible(ProductsPageLocators.BURGER_MENU_ICON)

@then('I see the shopping cart icon')
def step_impl(context):
    assert context.ProductsPage.is_element_visible(ProductsPageLocators.SHOPPING_CART_ICON)

@then('I see the filter dropdown menu')
def step_impl(context):
    assert context.ProductsPage.is_element_visible(ProductsPageLocators.FILTER_DROPDOWN_MENU)


@then('I see a list of items with titles, prices, descriptions, images and "add to cart" buttons')
def step_impl(context):
    items = context.browser.find_elements(*ProductsPageLocators.INVENTORY_LIST)
    for item in items:
        # Assert that the title, price, description, image, and button are visible within the item
        assert context.ProductsPage.is_element_visible(ProductsPageLocators.PRODUCT_TITLE)
        assert context.ProductsPage.is_element_visible(ProductsPageLocators.PRODUCT_PRICE)
        assert context.ProductsPage.is_element_visible(ProductsPageLocators.PRODUCT_DESCRIPTION)
        assert context.ProductsPage.is_element_visible(ProductsPageLocators.PRODUCT_IMAGE)
        assert context.ProductsPage.is_element_visible(ProductsPageLocators.ADD_TO_CART_BUTTON)

@when('I try to go to the inventory page')
def step_impl(context):
    context.browser.get(ProductsPage.url)

@then('I should be redirected to the login page')  #TODO: not a cool step. need a fixture for setup
def step_impl(context):
    assert context.browser.current_url == "https://www.saucedemo.com/"

@when('I click "Add to the cart" button on "(.*)" item')
def step_impl(context, product_name):
    context.ProductsPage.click_add_to_cart(product_name)

@then('I click "Remove" button on "(.*)" item')
def step_impl(context, product_name):
    context.ProductsPage.click_remove_from_cart(product_name)

@then('Shopping cart counter is not displayed')
def step_impl(context):
    assert not context.ProductsPage.is_element_visible(ProductsPageLocators.SHOPPING_CART_COUNTER)

@then('I see the shopping cart counter value as "(.*)"')
def step_impl(context, item_counter):
    assert int(item_counter) == context.ProductsPage.get_shopping_cart_counter_value()

@then('I click on shopping cart icon')
def step_impl(context):
    cart_button = context.browser.find_element(*ProductsPageLocators.SHOPPING_CART_ICON)
    cart_button.click()

@when('I select "(.*)" option in filter dropdown')
def step_impl(context, filter_option):
    context.ProductsPage.select_filter_option(filter_option)

@then('I see products sorted from A to Z')
def step_impl(context):
    assert context.ProductsPage.are_products_sorted_ascending()

@then('I see products sorted from Z to A')
def step_impl(context):
    assert context.ProductsPage.are_products_sorted_descending()

@then('I see products sorted by price from low to high')
def step_impl(context):
    assert context.ProductsPage.are_product_prices_sorted_ascending()

@then('I see products sorted by price from high to low')
def step_impl(context):
    assert context.ProductsPage.are_product_prices_sorted_descending()


