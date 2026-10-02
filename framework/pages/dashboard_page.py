from playwright.sync_api import Page
from framework.core.base_page import BasePage


class DashboardPage(BasePage):
    """Page Object for the OrangeHRM dashboard page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")
        self.user_menu = page.locator("span.oxd-userdropdown-tab")
        self.logout_link = page.get_by_role(
            "menuitem",
            name="Logout",
        )

    def logout(self) -> None:
        """Log out of OrangeHRM"""
        self.click(self.user_menu)
        self.click(self.logout_link)
