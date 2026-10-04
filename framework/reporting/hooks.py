import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store the test result on the pytest item."""

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        setattr(item, "rep_call", report)