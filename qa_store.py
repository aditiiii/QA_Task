import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://staging-scweb.arcapps.org/client-search")
    page.goto("https://staging-scweb.arcapps.org/")
    page.get_by_placeholder("Enter Your Username").click()
    page.get_by_placeholder("Enter Your Username").fill("tester")
    page.get_by_placeholder("Enter Your Password").click()
    page.get_by_placeholder("Enter Your Password").fill("tester2023!")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("combobox").first.select_option("1")
    page.get_by_role("combobox").nth(1).select_option("5")
    page.get_by_placeholder("Search facility").click()
    page.get_by_text("Dr Watson Dental Clinic").click()
    page.get_by_role("button", name="Enter").click()
    page.get_by_role("button", name="NRC").click()
    page.get_by_placeholder("Search by NRC").click()
    page.get_by_placeholder("Search by NRC").fill("111111/11/1_")
    page.get_by_role("button", name="search Search").click()
    page.get_by_role("button", name="Attend to Patient").click()
    page.get_by_role("link", name="Vital").click()
    page.get_by_role("button", name="Add Vital").click()
    page.get_by_placeholder("Enter Temperature (c)").click()
    page.get_by_placeholder("Enter Temperature (c)").fill("37")
    page.get_by_placeholder("Enter Systolic (mmHg)").click()
    page.get_by_placeholder("Enter Systolic (mmHg)").fill("99")
    page.get_by_placeholder("Enter Diastolic (mmHg)").click()
    page.get_by_placeholder("Enter Diastolic (mmHg)").fill("61")
    page.get_by_role("button", name="Save").click()
    page.locator("ul").filter(has_text="29-May-202429-May-202414:09:").get_by_role("button").click()
    page.get_by_role("button", name="Close").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
