import pytest
from playwright.sync_api import Browser, sync_playwright
from framework.core.config import Config


@pytest.fixture
def page(browser: Browser):
    """Provide a playwright page for each test"""
    context = browser.new_context()
    page = context.new_page()

    yield page
    context.close()


@pytest.fixture
def browser():
    with (sync_playwright() as playwright):
        if Config.BROWSER == "chromium":
            browser = playwright.chromium.launch(headless=Config.HEADLESS)
        elif Config.BROWSER == "firefox":
            browser = playwright.firefox.launch(headless=Config.HEADLESS)
        elif Config.BROWSER == "webkit":
            browser = playwright.webkit.launch(headless=Config.HEADLESS)
        else:
            raise ValueError(f"Unsupported browser: {Config.BROWSER}")

        yield browser

        browser.close()
