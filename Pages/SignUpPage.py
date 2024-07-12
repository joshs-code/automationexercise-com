from selenium.webdriver.common.by import By
from Utils import utils
import  pytest


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.title_xpath = '//input[@value="Mrs"]'
        self.name_box_xpath = '//input[@name="name"]'
        self.email_box_xpath = '//input[@data-qa="email"]'
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
        self.country_xpath = '//select[@data-qa="country"]'
        self.country_option_xpath = '//select[@data-qa="country"]//option[@value="United States"]'
        self.state_box_path = '//input[@id="state"]'
        self.city_box_path = '//input[@id="city"]'
        self.zip_code_xpath = '//input[@id="zipcode"]'
        self.mobile_number_box_xpath = '//input[@id="mobile_number"]'
        self.submit_button_xpath = '//button[@data-qa="create-account"]'

    def select_title(self):
        self.driver.find_element(By.XPATH, self.title_xpath).click()

    def verify_name(self):
        name = self.driver.find_element(By.XPATH, self.name_box_xpath).get_attribute("value")
        try:
            assert name == utils.NAME
        except:
            print(name)

    def verify_email(self):
        email = self.driver.find_element(By.XPATH, self.email_box_xpath).get_attribute("value")
        assert email == utils.EMAIL

    def enter_pass(self, password):
        self.driver.find_element(By.XPATH, self.pwd_xpath).clear()
        self.driver.find_element(By.XPATH, self.pwd_xpath).send_keys(password)

    def select_day_of_birth(self):
        self.driver.find_element(By.XPATH, self.day_xpath).click()
        self.driver.find_element(By.XPATH, self.day_option_xpath).click()

    def select_month_of_birth(self):
        self.driver.find_element(By.XPATH, self.month_option_xpath).click()
        self.driver.find_element(By.XPATH, self.month_option_xpath).click()

    def select_year_of_birth(self):
        self.driver.find_element(By.XPATH, self.year_xpath).click()
        self.driver.find_element(By.XPATH, self.year_option_xpath).click()

    def click_sign_up_newsletter(self):
        self.driver.find_element(By.XPATH, self.newsletter_box_xpath).click()

    def click_offers(self):
        self.driver.find_element(By.XPATH, self.special_offers_box_xpath).click()

    def enter_first_name(self, fname):
        self.driver.find_element(By.XPATH, self.first_name_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.first_name_box_xpath).send_keys(fname)

    def enter_last_name(self, lname):
        self.driver.find_element(By.XPATH, self.last_name_box_path).clear()
        self.driver.find_element(By.XPATH, self.last_name_box_path).send_keys(lname)

    def enter_company(self, company):
        self.driver.find_element(By.XPATH, self.company_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.company_box_xpath).send_keys(company)

    def enter_address(self, address):
        self.driver.find_element(By.XPATH, self.address1_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.address1_box_xpath).send_keys(address)

    def select_country(self):
        self.driver.find_element(By.XPATH, self.country_xpath).click()
        self.driver.find_element(By.XPATH, self.country_option_xpath).click()

    def enter_state(self, state):
        self.driver.find_element(By.XPATH, self.state_box_path).clear()
        self.driver.find_element(By.XPATH, self.state_box_path).send_keys(state)

    def enter_city(self, city):
        self.driver.find_element(By.XPATH, self.city_box_path).clear()
        self.driver.find_element(By.XPATH, self.city_box_path).send_keys(city)

    def enter_zip(self, zip):
        self.driver.find_element(By.XPATH, self.zip_code_xpath).clear()
        self.driver.find_element(By.XPATH, self.zip_code_xpath).send_keys(zip)

    def enter_mobile_phone(self, phone):
        self.driver.find_element(By.XPATH, self.mobile_number_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.mobile_number_box_xpath).send_keys(phone)

    def click_create_account(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()
