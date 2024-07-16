from selenium.webdriver.common.by import By
import pytest

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.user_title_sign_up_xpath = '//h2[text()="New User Signup!"]'
        self.name_input_field_xpath = '//input[@data-qa="signup-name"]'
        self.email_input_field_xpath = '//input[@data-qa="signup-email"]'
        self.signup_btn_xpath = '//button[@data-qa="signup-button"]'
        self.email_login_field_xpath = '//input[@data-qa="login-email"]'
        self.password_login_field_xpath = '//input[@data-qa="login-password"]'
        self.login_button_xpath = '//button[@type="submit" and @data-qa="login-button"]'
        self.driver_verify_login_text_xpath = '//h2[contains(text(),"Login to your account")]'
        self.driver_error_incorrect_email_or_pass_xpath = '//p[contains(text(), "Your email or password is incorrect!")]'

    def verify_signup_text(self):
        signup_text = self.driver.find_element(By.XPATH, self.user_title_sign_up_xpath).text
        assert signup_text == "New User Signup!"

    def enter_name(self, name):
        self.driver.find_element(By.XPATH, self.name_input_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.name_input_field_xpath).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_input_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_input_field_xpath).send_keys(email)

    def click_signup(self):
        self.driver.find_element(By.XPATH, self.signup_btn_xpath).click()

    def enter_login_email(self, email):
        self.driver.find_element(By.XPATH, self.email_login_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_login_field_xpath).send_keys(email)

    def enter_login_password(self, password):
        self.driver.find_element(By.XPATH, self.password_login_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_login_field_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def verify_login_into_account_txt(self):
        login_txt = self.driver.find_element(By.XPATH, self.driver_verify_login_text_xpath).text
        assert login_txt == "Login to your account"

    def verify_incorrect_error_msg(self):
        msg = self.driver.find_element(By.XPATH, self.driver_error_incorrect_email_or_pass_xpath).text
        assert msg == "Your email or password is incorrect!"