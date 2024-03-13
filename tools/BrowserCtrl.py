from tools.AppController import AppController
from behave import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from tools.config import FULLSCREEN, INCOGNITO, BASE_URL, APP_LOGS


@fixture
def run_browser(context):
    if context.browser == "chrome":
        options = webdriver.ChromeOptions()
        if FULLSCREEN:
            options.add_argument("--start-maximized")
        if INCOGNITO:
            options.add_argument("--incognito")
        if APP_LOGS:
            options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        context.driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=options)

    elif context.browser == "firefox":
        context.driver = webdriver.Firefox(service=webdriver.FirefoxService(GeckoDriverManager().install()))
        if FULLSCREEN:
            context.driver.maximize_window()

    elif context.browser == "edge":
        context.driver = webdriver.Edge(service=webdriver.EdgeService(EdgeChromiumDriverManager().install()))
        if FULLSCREEN:
            context.driver.maximize_window()

    else:
        raise ValueError("Unsupported browser: " + context.browser)

    context.driver.get(BASE_URL)
    context.app_controller = AppController(context.driver)

    yield

    context.driver.close()