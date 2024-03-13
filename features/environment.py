import logging
from behave import use_fixture
from tools.BrowserCtrl import run_browser
from tools.config import BROWSER


logging.basicConfig(filename="logs/logs_web.log",
                    filemode='a',
                    format='%(asctime)s.%(msecs)03d [%(levelname)s][%(name)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("Enviornment")


def before_all(context):
    logger.info('BEFORE ALL START')
    context.browser = BROWSER
    logger.info('BEFORE ALL END')


def before_feature(context, feature):
    logger.info('BEFORE FEATURE START')
    use_fixture(run_browser, context)
    logger.info('BEFORE FEATURE END')
