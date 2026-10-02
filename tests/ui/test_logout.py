from playwright.sync_api import expect

from framework.pages.dashboard_page import DashboardPage
from framework.pages.login_page import LoginPage


def test_successful_logout(
        login_page: LoginPage,
        dashboard_page: DashboardPage, ) -> None:
    login_page.open_home_page()
    login_page.login(username="Admin", password="admin123")

    expect(dashboard_page.dashboard_heading).to_be_visible()

    dashboard_page.logout()

    expect(login_page.login_button).to_be_visible()
