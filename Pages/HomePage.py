from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.signup_login_link_xpath = '//a[@href="/login"]'

    def click_signup_login_btn(self):
        self.driver.find_element(By.XPATH, self.signup_login_link_xpath).click()