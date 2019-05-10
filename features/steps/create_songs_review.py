
from behave import *

use_step_matcher("parse")

@when(u'I register comment')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register comment')


@then(u'I am viewing the details page for song by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for song by "user"')


@then(u'There are 1 comment')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 comment')


@given(u'I am not logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m not logged in')


@when(u'I register a new review at song "7 rings"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register a new review at song "7 rings"')


@then(u'I am redirected to the login form')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m redirected to the login form')


@then(u'There 0 comments')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There 0 comments')
