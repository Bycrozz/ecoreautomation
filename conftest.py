# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.test.pages.LoginPage import LoginPage


def pytest_addoption(parser):
    """
    Adds command-line options to pytest for headless mode and custom parallel sessions.
    """
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode.")


@pytest.fixture(scope="function")
def browser(request):
    """
    Setup Selenium WebDriver with options for headless mode and clean-up after each test.
    """
    headless = request.config.getoption("--headless")
    options = Options()

    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def open_login_page(browser):
    """
    Fixture to open the login page before each test.
    """
    login_page = LoginPage(browser)
    login_page.open_page()
    return login_page

