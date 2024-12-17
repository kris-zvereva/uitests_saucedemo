from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from features.page_model.shopping_cart_page import ShoppingCartPage

use_step_matcher('re')

@then('I am on shopping cart page')
def stem_impl(context):
    context.ShoppingCartPage = ShoppingCartPage(context.browser)
    assert context.browser.current_url == "https://www.saucedemo.com/cart.html"

@then('I see "(.*)" item in the cart')
def step_impl(context, item_title):
    item = context.ShoppingCartPage.get_item_locator(item_title)
    assert context.ShoppingCartPage.is_element_visible(item)

@then('I see no "(.*)" item in the cart')
def step_impl(context, item_title):
    item = context.ShoppingCartPage.get_item_locator(item_title)
    assert not context.ShoppingCartPage.is_element_visible(item)
