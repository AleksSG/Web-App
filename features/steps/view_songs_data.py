
from behave import *

use_step_matcher("parse")

@given(u'Exists an anonymous user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists an anonymous user')


@given(u'Exists information about one song, like "7 rings" registered by "admin"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists information about one song, like "7 rings" registered by "admin"')


@given(u'Exists an anonymous user or a registered user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists an anonymous user or a registered user')


@when(u'I view the details for song "7 rings"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I view the details for song "7 rings"')


@then(u'I\'m viewing song details including')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing song details including')
