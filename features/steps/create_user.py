from behave import *


use_step_matcher("parse")

@given(u'There is not user "user" registred')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given There is not user "user" registred')


@when(u'I click Register button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Register button')


@then(u'I fill')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I fill')


@then(u'User "user" is registred')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User "user" is registred')


@when(u'I register a user "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register a user "user"')


@then(u'I cannot register a new user "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I cannot register a new user "user"')
