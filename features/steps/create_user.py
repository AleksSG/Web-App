
from behave import *

use_step_matcher("parse")

@given(u'Not exists a user "user" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Not exists a user "user" with password "password"')

@given(u'Im not registered')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m not registered')


@when(u'I want to register')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I want to register')


@then(u'I\'m fill the data')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m fill the data')


@then(u'Now I\'m registered')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Now I\'m registered')

'''
@given(u'I\'m not registered')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m not registered')


@when(u'I register restaurant')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register restaurant')


@then(u'I\'m fill the data')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m fill the data')


@then(u'I can not register because the user already exists')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can not register because the user already exists')


@then(u'I need to fill the data again but with another user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I need to fill the data again but with another user')

'''
