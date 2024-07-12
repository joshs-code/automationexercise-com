from selenium.webdriver.common.by import By
from Utils import utils
import  pytest


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.title_xpath = '//input[@value="Mrs"]'
        self.name_box_xpath = '//input[@name="name"]'
        self.pwd_xpath = '//input[@data-qa="password"]'
        self.day_xpath = '//select[@name="days"]'
        self.day_option_xpath = '//select[@name="days"]//option[@value="3"]'
        self.month_xpath = '//select[@name="months"]'
        self.month_option_xpath = '//select[@name="months"]//option[@value="3"]'
        self.year_xpath = '//select[@name="years"]'
        self.year_option_xpath = '//select[@name="years"]//option[@value="1988"]'
        self.newsletter_box_xpath = '//input[@id="newsletter"]'
        self.special_offers_box_xpath = '//input[@id="optin"]'
        self.first_name_box_xpath = '//input[@name="first_name"]'
        self.last_name_box_path = '//input[@name="last_name"]'
        self.company_box_xpath ='//input[@name="company"]'
        self.address1_box_xpath = '//input[@name="address1"]'
        self.address2_box_xpath = '//input[@name="address2"]'
        self.country.xpath = '//select[@data-qa="country"]'
        self.country_option_xpath = '//select[@data-qa="country"]//option[@value="United States"]'
        self.state_box_path = '//input[@id="state"]'
        self.city_box_path = '//input[@id="city"]'
        self.zip_code_xpath = '//input[@id="zipcode"]'
        self.mobile_number_box_xpath = '//input[@id="mobile_number"]'
        self.submit_button_xpath = '//button[@data-qa="create-account"]'


    def select_title(self):
        self.driver.find_element(By.XPATH, self.title_xpath).click()

    def verify_name(self):
        name = self.driver.find_element(By.XPATH, self.name_box_xpath).text
        assert name == utils.NAME

    def verify_email(self):
        email = self.driver.find_element(By.XPATH, self.verify_email())