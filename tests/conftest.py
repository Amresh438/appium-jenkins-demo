import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APPIUM_URL = "http://127.0.0.1:4723"


@pytest.fixture
def driver():
    """Starts the Settings app before each test and closes it after."""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.android.settings"
    options.app_activity = ".Settings"
    options.no_reset = True

    drv = webdriver.Remote(APPIUM_URL, options=options)
    yield drv
    drv.quit()


@pytest.fixture(autouse=True)
def reports_folder():
    os.makedirs("reports", exist_ok=True)
