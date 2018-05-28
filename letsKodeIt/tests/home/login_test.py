from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Need to verify two verification points
    # 1 fails code will not go to the next verification point
    # If assert fails, it stop current test execution and
    # move to the next test method
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("parinitmishra9@gmail.com", "breakingbad")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title is Incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was not successful")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("parinitmishra9@gmail.com", "breakingbad1")
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", result, "Invalid login was not successful")