import pytest
from playwright.sync_api import Browser, sync_playwright
from framework.core.config import Config
import allure
from pathlib import Path


@pytest.fixture
def page(browser: Browser, request):
    """Provide a Playwright page for each test."""

    context = browser.new_context()
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    page = context.new_page()

    yield page

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot = page.screenshot()

        allure.attach(
            screenshot,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

        trace_path = Path("reports/traces") / f"{request.node.name}.zip"
        trace_path.parent.mkdir(parents=True, exist_ok=True)

        context.tracing.stop(path=str(trace_path))

        allure.attach.file(
            trace_path,
            name="Playwright Trace",
            attachment_type=allure.attachment_type.ZIP,
        )

    else:
        context.tracing.stop()

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
