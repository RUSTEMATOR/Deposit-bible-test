import time
import pytest
import subprocess
from mapping import email_mapping, country_translations
from playwright.sync_api import Playwright, sync_playwright, expect

vpn_locations = [
    "NZ", "AU", "AT", "CH", "IE", "NO", "CY", "DE", "DK", "ZA",
    "PH", "JP", "IN",
    "IT", "LU", "BR",
    "SI", "IS", "KR", "MX", "AR", "CL", "KH", "BD", "TW", "LA"
]

vpn_locations_mga = ["DE", "DK", "CY", "CA","NZ", "AT", "CH", 
                     "LU", "IE", "BG"]

def change_vpn(vpn_location):
    command = f"expresso connect {vpn_location}"
    subprocess.run(command, shell=True)

def teardown():
    command = f"expresso disconnect"
    subprocess.run(command, shell=True)

@pytest.mark.flaky(reruns=3, reruns_delay=1)
@pytest.mark.parametrize("vpn_location", vpn_locations)
def test_deposit_bible(playwright: Playwright, vpn_location: str) -> None:
    print(f"Changing VPN to: {vpn_location}")
    change_vpn(vpn_location)
    time.sleep(5)
    print("VPN changed successfully")
    
    browser = playwright.chromium.launch(headless=False,)
    context = browser.new_context()
    page = context.new_page()
    
    current_country = vpn_location  # Adjust this dynamically based on your application's state
    current_translations = country_translations[current_country]["translations"]
    current_email = email_mapping[current_country]
    
    page.goto("https://www.kingbillycasino.com")
    page.get_by_role("link", name=current_translations["login"]).click()
    page.get_by_placeholder(current_translations["email_placeholder"]).click()
    page.get_by_placeholder(current_translations["email_placeholder"]).fill(current_email)
    page.get_by_placeholder(current_translations["password_placeholder"]).click()
    page.get_by_placeholder(current_translations["password_placeholder"]).fill("LOL12lol")
    page.get_by_placeholder(current_translations["password_placeholder"]).press("Enter")
    time.sleep(4)
    page.get_by_role("button", name=current_translations["deposit_button"]).click()
    page.screenshot(path=f"Desktop/Deposit bible screenshots/CU/{vpn_location}/{vpn_location} deposit.png")
    page.locator("payments-tabs button").nth(4).click()
    page.get_by_role("banner").get_by_role("link").first.click()
    page.get_by_role("link", name=current_translations["my_account"]).click()
    page.get_by_role("link", name=current_translations["wallet_link"]).click()
    page.get_by_role("link", name=current_translations["withdrawal_link"]).click()
    time.sleep(5)
    page.screenshot(path=f"Desktop/Deposit bible screenshots/CU/{vpn_location}/{vpn_location} withdrawal.png")
    
    
    teardown()
    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()

@pytest.mark.flaky(reruns=3, reruns_delay=1)
@pytest.mark.parametrize("vpn_location", vpn_locations_mga)
def test_deposit_bible_mga(playwright: Playwright, vpn_location: str) -> None:
    print(f"Changing VPN to: {vpn_location}")
    change_vpn(vpn_location)
    time.sleep(5)
    print("VPN changed successfully")
    
    browser = playwright.chromium.launch(headless=False,)
    context = browser.new_context()
    page = context.new_page()
    
    current_country = vpn_location  # Adjust this dynamically based on your application's state
    current_translations = country_translations[current_country]["translations"]
    current_email = email_mapping[current_country]
    
    page.goto("https://www.kingbilly.com")
    page.get_by_role("link", name=current_translations["login"]).click()
    page.get_by_placeholder(current_translations["email_placeholder"]).click()
    page.get_by_placeholder(current_translations["email_placeholder"]).fill(current_email)
    page.get_by_placeholder(current_translations["password_placeholder"]).click()
    page.get_by_placeholder(current_translations["password_placeholder"]).fill("LOL12lol!")
    page.get_by_placeholder(current_translations["password_placeholder"]).press("Enter")
    if page.frame_locator("iframe[name=\"intercom-banner-frame\"]").get_by_label("Close").is_visible():
       page.frame_locator("iframe[name=\"intercom-banner-frame\"]").get_by_label("Close").click()

    time.sleep(4)
    page.get_by_role("button", name=current_translations["deposit_button"]).click()
    time.sleep(10)
    page.screenshot(path=f"Desktop/Deposit bible screenshots/MGA/{vpn_location}/{vpn_location} deposit.png")
    page.locator("payments-tabs button").nth(4).click()
    page.get_by_role("banner").get_by_role("link").first.click()
    page.get_by_role("link", name=current_translations["my_account"]).click()
    page.get_by_role("link", name=current_translations["wallet_link"]).click()
    page.get_by_role("link", name=current_translations["withdrawal_link"]).click()
    time.sleep(5)
    page.screenshot(path=f"Desktop/Deposit bible screenshots/MGA/{vpn_location}/{vpn_location} withdrawal.png")
    
    
    teardown()
    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()
