from tabnanny import check

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.devtools.v85.page import wait_for_debugger

from features.locators.products_page import ProductsPageLocators
from features.locators.shopping_cart_page import ShoppingCartPageLocators
from features.page_model.shopping_cart_page import ShoppingCartPage

use_step_matcher('re')

@when('I am on shopping cart page')
def stem_impl(context):
    context.ShoppingCartPage = ShoppingCartPage(context.browser)
    assert context.browser.current_url == "https://www.saucedemo.com/cart.html"

@when('I click on shopping cart icon')
def step_impl(context):
    cart_button = context.browser.find_element(*ProductsPageLocators.SHOPPING_CART_ICON)
    cart_button.click()

@then('I click "Continue Shopping" button')
def step_impl(context):
    cont_button = context.browser.find_element(*ShoppingCartPageLocators.CONTINUE_SHOPPING_BUTTON)
    cont_button.click()

@then('I click "Checkout" button')
def step_impl(context):
    check_button = context.browser.find_element(*ShoppingCartPageLocators.CHECKOUT_BUTTON)
    check_button.click()

@then('I see "(.*)" item in the cart')
def step_impl(context, item_title):
    item = context.ShoppingCartPage.get_item_locator(item_title)
    assert context.ShoppingCartPage.is_element_visible(item)


@then('I see no "(.*)" item in the cart')
def step_impl(context, item_title):
    item = context.ShoppingCartPage.get_item_locator(item_title)
    assert not context.ShoppingCartPage.is_element_visible(item)

@then('I see shopping cart is empty')
def step_impl(context):
    assert not context.ShoppingCartPage.is_element_visible(ShoppingCartPageLocators.CART_ITEM)

@when('I try to go to the shopping cart page')
def step_impl(context):
    context.browser.get(ShoppingCartPage.url)

@then('I click "Remove" button')
def step_impl(context):
    button = context.browser.find_element(*ShoppingCartPageLocators.REMOVE_BUTTON)
    button.click()
