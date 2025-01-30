from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from features.page_model.checkout_page import CheckoutPage

@when('I try to go to the checkout page')
def step_impl(context):
    context.browser.get(CheckoutPage.url)

@then('I am on the checkout1 page')
def stem_impl(context):
    context.CheckoutPage = CheckoutPage(context.browser)
    assert context.browser.current_url == "https://www.saucedemo.com/checkout-step-one.html"