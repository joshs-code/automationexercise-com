import pytest
from Utils import utils
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.SignUpPage import SignUpPage
from Pages.AccountCreatedPage import AccountCreatedPage
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

        sp = SignUpPage(driver)
        sp.select_title()
        sp.verify_name()
        sp.verify_email()
        sp.enter_pass(utils.PASSWORD)
        sp.select_day_of_birth()
        sp.select_month_of_birth()
        sp.select_year_of_birth()
        sp.click_sign_up_newsletter()
        sp.click_offers()
        sp.enter_first_name(utils.NAME)
        sp.enter_last_name(utils.LASTNAME)
        sp.enter_company(utils.COMPANY)
        sp.enter_address(utils.ADDRESS)
        sp.select_country()
        sp.enter_city(utils.CITY)
        sp.enter_state(utils.STATE)
        sp.enter_zip(utils.ZIP)
        sp.enter_mobile_phone(utils.MOBILE)
        sp.click_create_account()

        acp = AccountCreatedPage(driver)
        acp.verify_account_txt()
        acp.click_continue_btn()

        hp.verify_logged_in()
        hp.delete_account()
        hp.verify_account_deletion()