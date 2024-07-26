import pytest
import time
import config
from pages.WelcomePage import WelcomePage
from playwright.sync_api import Playwright
from methods import CustomMethods
from evpn import ExpressVpnApi

@pytest.mark.parametrize("account_key, username, password, url, deposit_url, withdrawal_url", [(key, val['username'],
                                                              val['password'], val['url'], val['deposit_url'], val['withdrawal_url']) for key, val in config.accounts.items()])
def test(playwright: Playwright, account_key, username, password, url, deposit_url, withdrawal_url):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1800, "height": 1000})
    page = context.new_page()
    try:
        with ExpressVpnApi() as api:
            locations = api.locations  # get available locations
            loc = next((location for location in locations if location["country_code"] == account_key), None)
            api.connect(loc["id"])

        email = config.accounts[account_key]['username']
        password = config.accounts[account_key]['password']
        url = config.accounts[account_key]['url']
        deposit_url = config.accounts[account_key]['deposit_url']
        withdrawal_url = config.accounts[account_key]['withdrawal_url']

        welcome_page = WelcomePage(page)
        methods = CustomMethods(page)

        methods.visit_page(url)

        welcome_page.login(email, password)

        welcome_page.click_deposit_button()
        time.sleep(20)

        methods.capture_screenshot(account_key, "Deposit", "Deposit", account_key)

        methods.visit_page(deposit_url)
        time.sleep(20)
        methods.capture_screenshot(account_key, "Deposit_Profile", "Deposit_profile", account_key)

        methods.visit_page(withdrawal_url)
        time.sleep(20)
        methods.capture_screenshot(account_key, "Withdrawal", "Withdrawal", account_key)

        browser.close()


    except:
        browser.close()
        api.disconnect()
        raise AssertionError




@pytest.mark.parametrize("account_key, username, password, url, deposit_url, withdrawal_url", [(key, val['username'],
                                                              val['password'], val['url'], val['deposit_url'], val['withdrawal_url']) for key, val in config.accounts_old.items()])
def test_old(playwright: Playwright, account_key, username, password, url, deposit_url, withdrawal_url):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1800, "height": 1000})
    page = context.new_page()
    try:
        with ExpressVpnApi() as api:
            locations = api.locations  # get available locations
            loc = next((location for location in locations if location["country_code"] == account_key), None)
            api.connect(loc["id"])

        email = config.accounts_old[account_key]['username']
        password = config.accounts_old[account_key]['password']
        url = config.accounts_old[account_key]['url']
        deposit_url = config.accounts_old[account_key]['deposit_url']
        withdrawal_url = config.accounts_old[account_key]['withdrawal_url']

        welcome_page = WelcomePage(page)
        methods = CustomMethods(page)

        methods.visit_page(url)

        welcome_page.login(email, password)

        welcome_page.click_deposit_button()
        time.sleep(20)

        methods.capture_screenshot_old(account_key, "Deposit", "Deposit", account_key)

        methods.visit_page(deposit_url)
        time.sleep(20)
        methods.capture_screenshot_old(account_key, "Deposit_Profile", "Deposit_profile", account_key)

        methods.visit_page(withdrawal_url)
        time.sleep(20)
        methods.capture_screenshot_old(account_key, "Withdrawal", "Withdrawal", account_key)

        browser.close()


    except:
        browser.close()

        raise AssertionError

