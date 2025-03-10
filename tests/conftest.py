import os
from datetime import datetime

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

# @pytest.fixture(scope="session", autouse=True)
# def load_env():
#     load_dotenv()
#     selenoid_login = os.getenv("SELENOID_LOGIN")
#     selenoid_pass = os.getenv("SELENOID_PASS")
#     selenoid_url = os.getenv("SELENOID_URL")
#
#     print(selenoid_login)

@pytest.fixture(scope="function", autouse=True)
def browser_config(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user_k:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.base_url = "https://demoqa.com/automation-practice-form"
    browser.config.type_by_js = True
    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()

    # driver_options = webdriver.ChromeOptions()
    # driver_options.page_load_strategy = "eager"
    # browser.config.driver_options = driver_options
    #
    # browser.config.window_height = 2500
    # browser.config.window_width = 1400


@pytest.fixture(scope="function")
def today_date():
    c = datetime.now()
    current_time = c.strftime("%d %B, %Y")
