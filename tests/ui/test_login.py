import pytest
from playwright.sync_api import expect

from framework.pages.dashboard_page import DashboardPage
from test_data.login_data import LOGIN_TEST_DATA, LoginTestData

from framework.pages.login_page import LoginPage


@pytest.mark.parametrize(
    "test_data",
    LOGIN_TEST_DATA,
    ids=lambda test_data: test_data.test_id,

)
def test_login_validation(login_page: LoginPage, test_data: LoginTestData):
    login_page.open_home_page()
    login_page.submit_login(test_data.username, test_data.password)

    expected_locators = {

        "Invalid credentials": login_page.invalid_credentials_message,
        "Required": login_page.required_message

    }

    expected_locator = expected_locators[test_data.expected_result]

    expect(expected_locator).to_be_visible()


def test_successful_login(login_page: LoginPage) -> None:
    login_page.open_home_page()
    login_page.login(username="Admin", password="admin123")

    dashboard_page = DashboardPage(login_page.page)

    expect(dashboard_page.dashboard_heading).to_be_visible()
