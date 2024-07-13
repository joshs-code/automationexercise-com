from selenium.webdriver.common.by import By


class AccountCreatedPage:

    def __init__(self, driver):
        self.driver = driver
        self.account_created_text_xpath = '//h2[@data-qa="account-created"]//b'
        self.continue_btn_xpath = '//a[@data-qa="continue-button"]'

    def verify_account_txt(self):
        account_creation_title = self.driver.find_element(By.XPATH, self.account_created_text_xpath).text
        assert account_creation_title == "ACCOUNT CREATED!"

    def click_continue_btn(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()