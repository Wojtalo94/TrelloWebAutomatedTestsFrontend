import logging
from .Request import Request
from pages.base_page import BasePage
from tools.AppLogAnalyzer import AppLogAnalyzer
from tools.RestController import RestController


class AppController():
    def __init__(self, driver):
        self._logger = logging.getLogger("AppController")
        self.driver = driver
        self._request = Request()
        self.rest_controller = RestController()
        self._base_page = BasePage(driver)
        self._app_log_analyzer = AppLogAnalyzer(driver)
        
    def log_in(self):
        self._logger.info("Log in user in web app")
        self._base_page.click_log_in_button().fill_email().click_submit_login()
        self._base_page.fill_password().click_submit_login().wait_for_main_page()