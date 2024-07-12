import pytest
from Utils import utils
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
import time


@pytest.mark.usefixtures("test_setup")
class TestRegisterUser:

    def test_verify_homepage(self):
        driver = self.driver
        driver.get(utils.URL)
        assert driver.title == "Automation Exercise"

    def test_register_user(self):
        driver = self.driver

        hp = HomePage(driver)
        hp.click_signup_login_btn()

        lp = LoginPage(driver)
        lp.enter_name(utils.NAME)
        lp.enter_email(utils.EMAIL)
        lp.click_signup()
