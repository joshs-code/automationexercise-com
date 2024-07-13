from selenium.webdriver.common.by import By
import Utils
import Utils.utils
import time

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.signup_login_link_xpath = '//a[@href="/login"]'
        self.logged_in_xpath = '//li//a[contains(text(), "Logged in as")]'
        self.delete_account_xpath = '//li//a[@href="/delete_account"]'
        self.confirm_delete_xpath = '//h2//b[contains( text(), "Account Deleted!")]'

    def click_signup_login_btn(self):
        self.driver.find_element(By.XPATH, self.signup_login_link_xpath).click()

    def verify_logged_in(self):
        logged_in = self.driver.find_element(By.XPATH, self.logged_in_xpath).text
        assert logged_in == f"Logged in as {Utils.utils.NAME}"

    def delete_account(self):
        self.driver.find_element(By.XPATH, self.delete_account_xpath).click()

    def verify_account_deletion(self):
        msg_deletion = self.driver.find_element(By.XPATH, self.confirm_delete_xpath).text
        assert msg_deletion == "ACCOUNT DELETED!"
        time.sleep(3)