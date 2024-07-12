from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.user_title_sign_up_xpath = '//h2[text()="New User Signup!"]'
        self.name_input_field_xpath = '//input[@data-qa="signup-name"]'
        self.email_input_field_xpath = '//input[@data-qa="signup-email"]'
        self.signup_btn_xpath = '//button[@data-qa="signup-button"]'

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