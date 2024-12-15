from features.locators.login_page import LoginPageLocators


class LoginPage:
    url = "https://www.saucedemo.com/"

    def __init__(self, browser):
        self.browser = browser

    def enter_username(self, username):
        username_input = self.browser.find_element(*LoginPageLocators.USERNAME_INPUT)  # Since USERNAME_INPUT is a tuple (By.ID, "user-name"), you must use * to unpack the tuple into two arguments when calling find_element
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def press_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def get_error_message(self):
        error_message = self.browser.find_element(*LoginPageLocators.ERROR_MESSAGE)
        return error_message.text
