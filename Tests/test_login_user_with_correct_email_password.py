import pytest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utils import  utils
@pytest.mark.usefixtures("test_setup")
class TestRegisterUserCorrect:

    def test_verify_homepage(self):
        driver = self.driver
        driver.get(utils.URL)
        assert driver.title == "Automation Exercise"

        hp = HomePage(driver)
        hp.click_signup_login_btn()

    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_login_email(utils.EMAIL)
        lp.enter_login_password(utils.PASSWORD)
        lp.click_login_button()

    def test_delete_account(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.delete_account()
        hp.verify_account_deletion()
