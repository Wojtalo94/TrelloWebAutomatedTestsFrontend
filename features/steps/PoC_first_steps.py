from behave import Given
import logging

logger = logging.getLogger("PoC first test")


@Given("The user has been logged in")
def step_impl(context):
    context.app_controller.log_in()