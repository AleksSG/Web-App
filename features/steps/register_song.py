
from behave import *

use_step_matcher("parse")

@given(u'Exists an admin "admin" with password "admin"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists an admin "admin" with password "admin"')


@given(u'I login as admin "admin" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I login as admin "admin" with password "password"')


@when(u'I register song')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register song')


@then(u'I\'m viewing the details page for song by "admin"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for song by "admin"')


@then(u'There are 1 song')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 song')


@then(u'I\'m viewing the details page for song by "admin"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for song by "admin"')


@then(u'I see that the song is already register')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see that the song is already register')


@given(u'I\'m a registered or an anonymous user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m a registered or an anonymous user')


@when(u'I try to register song')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I try to register song')


@then(u'I can not do it because I\'m not an admin')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can not do it because I\'m not an admin')


@then(u'There are 0 songs')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 0 songs')
