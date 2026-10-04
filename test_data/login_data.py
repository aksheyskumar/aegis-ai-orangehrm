from dataclasses import dataclass


@dataclass(frozen=True)
class LoginTestData:
    test_id: str
    username: str
    password: str
    expected_result: str


LOGIN_TEST_DATA = [
    LoginTestData(
        test_id="invalid_credentials",
        username="Admin",
        password="Bajaj123",
        expected_result="Invalid credentials",
    ),
    LoginTestData(
        test_id="missing_password",
        username="Admin",
        password="",
        expected_result="Required",
    ),
    LoginTestData(
        test_id="missing_username",
        username="",
        password="admin123",
        expected_result="Required",
    ),
    LoginTestData(
        test_id="invalid_username",
        username="Bajaj",
        password="admin123",
        expected_result="Invalid credentials",
    ),

]
