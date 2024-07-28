import os
import time
import pytest
import subprocess
import config
from playwright.sync_api import Page, expect
from datetime import datetime



class CustomMethods(Page):
    def __init__(self, page: Page):
        self.page = page

    def capture_screenshot(self, locale, profile_position, name, account_key):
        # Adjusted base directory to include 'Promo_placement'
        base_dir = "Screenshots"
        # Adjusted date format to 'DD.MM.YYYY'
        date_str = datetime.now().strftime("%d.%m.%Y")
        # Adjusted directory path to include 'locale' and 'screenshot_name' for promo placement
        dir_path = os.path.join(base_dir, date_str, locale, profile_position)

        # Ensure the directory exists
        os.makedirs(dir_path, exist_ok=True)

        counter = 1

        # Construct the screenshot path with a generic filename or a specific naming convention
        screenshot_path = os.path.join(dir_path, f"{account_key}_{name}.png")

        # Check if the screenshot file already exists and increment the counter until a unique filename is found
        while os.path.exists(screenshot_path):
            counter += 1
            screenshot_path = os.path.join(dir_path, f"{locale}_{profile_position}_{counter}.png")

        self.page.screenshot(path=screenshot_path, full_page=False)
        return screenshot_path

    def capture_screenshot_old(self, locale, profile_position, name, account_key):
        # Adjusted base directory to include 'Promo_placement'
        base_dir = "Screenshots_old"
        # Adjusted date format to 'DD.MM.YYYY'
        date_str = datetime.now().strftime("%d.%m.%Y")
        # Adjusted directory path to include 'locale' and 'screenshot_name' for promo placement
        dir_path = os.path.join(base_dir, date_str, locale, profile_position)

        # Ensure the directory exists
        os.makedirs(dir_path, exist_ok=True)

        counter = 1

        # Construct the screenshot path with a generic filename or a specific naming convention
        screenshot_path = os.path.join(dir_path, f"({account_key}_{name}_old.png")

        # Check if the screenshot file already exists and increment the counter until a unique filename is found
        while os.path.exists(screenshot_path):
            counter += 1
            screenshot_path = os.path.join(dir_path, f"{locale}_{profile_position}_old.png")

        self.page.screenshot(path=screenshot_path)
        return screenshot_path

    # @pytest.mark.parametrize("locale, username, password", [(key, val['locale'], val['username'], val['password']) for key, val in config.accounts])


    def visit_page(self, link):
        self.page.goto(link)

    def click_on(self, locator):
        self.page.locator(locator).click()

    def fill_in(self, locator, value):
        self.page.locator(locator).fill(value)

    def click_on_xpath(self, xpath):
        self.page.locator(xpath).click()

    def check_to_be_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible(timeout=100000000)

    def check_not_visible(self, locator):
        return self.page.locator(locator).is_hidden()