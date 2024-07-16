import pytest
from Utils import utils
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
import names

@pytest.mark.usefixtures("test_setup")
class TestLoginUserIncorrectEmailPassword:

    def test_verify_homepage(self):
        driver = self.driver
        driver.get(utils.URL)
        hp = HomePage(driver)
        title = driver.title
        assert title == "Automation Exercise"
        hp.click_signup_login_btn()

    def test_login_incorrect(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.verify_signup_text()
        email = names.get_first_name() + '@gmail.com'
        lp.enter_login_email(email)
        lp.enter_login_password(names.get_first_name())
        lp.click_login_button()
        lp.verify_incorrect_error_msg()