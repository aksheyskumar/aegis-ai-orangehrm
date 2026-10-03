from playwright.sync_api import Page
from framework.core.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the OrangeHRM login page."""
    LOGIN_PATH = "/web/index.php/auth/login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_field = page.get_by_role("textbox", name="Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

        self.invalid_credentials_message = page.get_by_text(
            "Invalid credentials",
            exact=True,
        )

        self.required_message = page.get_by_text(
            "Required",
            exact=True,
        )

    def login(self, username: str, password: str) -> None:
        """Log in to OrangeHRM with the provided credentials."""
        self.submit_login(username, password)

    def open_home_page(self) -> None:
        """Open the Orange HRM login page"""
        self.navigate(self.LOGIN_PATH)

    def submit_login(self, username: str, password: str) -> None:
        """Submit the orange HRM login form"""
        self.fill(self.username_field, username)
        self.fill(self.password_field, password)
        self.click(self.login_button)
