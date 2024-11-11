import pytest
from src.test.utils.TestUtils import TestUtils


@pytest.mark.usefixtures("browser")
class TestLogin(TestUtils):

    @pytest.mark.parametrize("login_data", TestUtils.load_test_data("src/test/testData/loginData.json", "valid_login"))
    @pytest.mark.valid_login
    def test_valid_login(self, login_data, open_login_page):
        """
        Open the login page, log with the username and password from the Json data file and assert if the login is successful.
        """
        username = login_data["username"]
        password = login_data["password"]
        open_login_page.login(username, password)
        assert open_login_page.verify_successful_login(), f"Expected login to succeed with {username}:{password}"

    @pytest.mark.parametrize("login_data", TestUtils.load_test_data("src/test/testData/loginData.json", "invalid_login"))
    @pytest.mark.invalid_login
    def test_invalid_login(self, login_data, open_login_page):
        """
        Open the login page, log with the username and password from the Json data file and assert if the error message is displayed.
        """
        username = login_data["username"]
        password = login_data["password"]
        open_login_page.login(username, password)
        assert open_login_page.verify_failed_login(), f"Expected login to fail with {username}:{password}"
