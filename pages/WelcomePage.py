from playwright.async_api import Playwright, Page, Browser, BrowserContext
import pytest
import config


class WelcomePage:
    def __init__(self, page: Page):
        self.page = page

        self.login_button = page.locator('.header__button--sign-in')
        self.email_input = page.locator('.login-form__input > .input__native')
        self.password_input = page.locator('div.login-form__input.password-input > div > input')
        self.login_submit_button = page.locator('.login-form__submit-button')
        self.deposit_button = page.locator('.header__deposit.deposit-button')


    def fill(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def login(self, email, password):
        self.login_button.click()
        self.fill(email, password)
        self.login_submit_button.click()


    def click_deposit_button(self):
        self.deposit_button.click()

    def append_url_to_file(self, file_path):
        with open(file_path, 'a') as file:
            file.write(self.page.url + '\n')
