from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from features.page_model.login_page import LoginPage

use_step_matcher('re')

@given('I am on the login page')
def step_impl(context):
    service = Service('/Users/kristinazvereva/chromedriver')
    context.browser = webdriver.Chrome(service=service)
    context.LoginPage = LoginPage(context.browser)
    context.browser.get(LoginPage.url)

@when('I enter "(.*)" in the "Username" field')
def step_impl(context, username):
    context.LoginPage.enter_username(username)

@when('I enter "(.*)" in the "Password" field')
def step_impl(context, password):
    context.LoginPage.enter_password(password)

@when('I press "Login" button')
def step_impl(context):
    context.LoginPage.press_login_button()

@then('I am on the shop page')
def step_impl(context):
    assert context.browser.current_url == "https://www.saucedemo.com/inventory.html"
    context.browser.quit()
