
from behave import *

use_step_matcher("parse")

@given(u'Exists a admin "admin" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists a admin "admin" with password "password"')


@given(u'Exists song registered by "admin"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists song registered by "admin"')


@given(u'I login as admin "admin" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I login as admin "admin" with password "password"')


@when(u'I edit the song with name "7 rings"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit the song with name "7 rings"')


@then(u'I\'m viewing the details page for song by "admin"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for song by "admin"')


@then(u'There are 1 songs')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 songs')


@given(u'I\'m not an admin')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m not an admin')


@when(u'I view the details for song "7 rings"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I view the details for song "7 rings"')


@then(u'There is no "edit" link available')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There is no "edit" link available')
