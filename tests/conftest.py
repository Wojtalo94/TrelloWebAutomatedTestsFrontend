import pytest
import logging
from selenium import webdriver
from tools.config import HEADLESS, FULLSCREEN, REMOTE_MODE, INCOGNITO, APP_LOGS
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Remote
from pages.home_page import HomePage

logging.basicConfig(filename="logs/logs_web.log",
                    filemode='a',
                    format='%(asctime)s.%(msecs)03d [%(levelname)s][%(name)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("Enviornment")


@pytest.fixture()
def driver(request):
    driver = remote_chromedriver() if REMOTE_MODE else local_chromedriver()
    request.cls.driver = driver

    yield driver
    driver.quit()


def local_chromedriver():
    options = chrome_options()
    # below old not working code
    # chrome_driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=options)
    # below working code for webdriver in 4.0.2 version
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def remote_chromedriver() -> Remote:
    wd_hub = "http://selenium__standalone-chrome:4444/wd/hub"
    options = chrome_options()
    chrome_driver = webdriver.Remote(command_executor=wd_hub, options=options)
    return chrome_driver


def chrome_options():
    options = webdriver.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    if FULLSCREEN:
        options.add_argument("--start-fullscreen")
    if INCOGNITO:
        options.add_argument("--incognito")
    if APP_LOGS:
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    return options

@pytest.fixture()
def login(driver):
    logger.info("Log in user in web app")
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_log_in_button().fill_email().click_submit_login()
    home_page.fill_password().click_submit_login().wait_for_main_page()
