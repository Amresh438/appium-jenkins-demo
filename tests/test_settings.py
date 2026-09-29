import time


def test_settings_app_opens(driver):
    """App launches and the correct app is in the foreground."""
    assert driver.current_package == "com.android.settings"


def test_screen_has_content(driver):
    """The screen loaded some UI elements."""
    time.sleep(2)
    assert len(driver.page_source) > 500


def test_take_screenshot(driver):
    """Saves a screenshot into the reports folder."""
    time.sleep(2)
    saved = driver.get_screenshot_as_file("reports/settings_screen.png")
    assert saved is True


def test_press_back_and_home(driver):
    """Press the Back key, then the Home key (leaves the app)."""
    driver.back()
    driver.press_keycode(3)  # 3 = HOME key
    time.sleep(1)
    assert driver.current_package != "com.android.settings"
