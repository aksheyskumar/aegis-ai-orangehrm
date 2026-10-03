from playwright.sync_api import Locator, Page
from framework.core.config import Config


class BasePage:
    """Base Page Object containing common Playwright interactions."""

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: Locator) -> None:
        """Click the specified element."""
        locator.click()

    def fill(self, locator: Locator, text: str) -> None:
        """Fill the specified input element with text."""
        locator.fill(text)

    def get_text(self, locator: Locator) -> str | None:
        """Return the text content of the specified element."""
        return locator.text_content()

    def navigate(self, url: str) -> None:
        """Navigate to the specified URL."""
        self.page.goto(f"{Config.BASE_URL}{url}",wait_until="domcontentloaded",)
