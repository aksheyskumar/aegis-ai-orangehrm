from framework.fixtures.browser import browser, page
import pytest
from playwright.sync_api import Page
from framework.pages.login_page import LoginPage
from framework.pages.dashboard_page import DashboardPage

pytest_plugins = ["framework.reporting.hooks"]


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)
