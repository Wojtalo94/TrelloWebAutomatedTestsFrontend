from behave import Given, Then
import logging

logger = logging.getLogger("PoC first test")


@Given("The user has been logged in")
def step_impl(context):
    context.app_controller.log_in()


@Then("The user was logged in as {member_type}")
def step_impl(context, member_type):
    status = context.app_controller.rest_controller.check_member_type()
    assert status == member_type, f"Wrong member type: {status}, should be: {member_type}"


@Then("The user is not deactivated")
def step_impl(context):
    status = context.app_controller.rest_controller.check_member_deactivation()
    assert status == False, f"Wrong member status: {status}, should be: False"