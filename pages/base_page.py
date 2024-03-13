import logging
from tools.config import MAX_WAIT
from tools.user_data import UserData
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _log_in_field = (By.CSS_SELECTOR, "a[data-uuid*='login']")
    _email_field = (By.CSS_SELECTOR, "input[id='username']")
    _submit_login_field = (By.CSS_SELECTOR, "button[id='login-submit']")
    _password_field = (By.CSS_SELECTOR, "input[id='password']")
    _without_two_step_verification_field = (By.CSS_SELECTOR, "button[id='mfa-promote-continue']")
    _main_page_field = (By.CSS_SELECTOR, "h3[class='boards-page-section-header-name']")

    def __init__(self, driver):
        self._logger = logging.getLogger("Base Page")
        self.driver = driver
        self.ec = ec
        self.wait = WebDriverWait(driver, MAX_WAIT)
        self.user_data = UserData("tools/user_data.csv")

    def click_log_in_button(self):
        self._logger.info("Click log in button")
        self.wait.until(self.ec.element_to_be_clickable(self._log_in_field)).click()
        return self
    
    def fill_email(self):
        self._logger.info("Fill email with data")
        self.wait.until(self.ec.visibility_of_element_located(self._email_field))
        _emial = self.user_data.get_user_data('EMAIL')
        self.driver.find_element(*self._email_field).send_keys(_emial)
        return self
    
    def click_submit_login(self):
        self._logger.info("Click submit login button")
        self.wait.until(self.ec.element_to_be_clickable(self._submit_login_field)).click()
        return self
    
    def fill_password(self):
        self._logger.info("Fill password with data")
        self.wait.until(self.ec.visibility_of_element_located(self._password_field))
        _password = self.user_data.get_user_data('PASSWORD')
        self.driver.find_element(*self._password_field).send_keys(_password)
        return self
    
    def click_without_two_step_verification(self):
        self._logger.info("Click without two step verification button")
        self.wait.until(self.ec.element_to_be_clickable(self._without_two_step_verification_field)).click()
        return self
    
    def wait_for_main_page(self):
        self._logger.info("Wait for loading main page")
        self.wait.until(self.ec.visibility_of_element_located(self._main_page_field))
        return self