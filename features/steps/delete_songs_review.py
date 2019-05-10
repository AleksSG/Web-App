
from behave import *

use_step_matcher("parse")

@given(u'Exists song registered by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists song registered by "user"')


@given(u'Exists review at song "7 rings" by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists review at song "7 rings" by "user"')


@when(u'I delete a review at song "7 rings"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I delete a review at song "7 rings"')


@then(u'I\'m viewing the details page for song by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for song by "user"')


@then(u'The list contains 0 review')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The list contains 0 review')


@then(u'There are 0 comment')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 0 comment')


@given(u'Exists review at song "7 rings" by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists review at song "7 rings" by "user1"')


@when(u'I try to delete a review at song "7 rings" by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I try to delete a review at song "7 rings" by "user1"')


@then(u'I ("user2") can not edit the review')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I ("user2") can not edit the review')


@then(u'The list contains 1 review')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The list contains 1 review')


@then(u'There are 1 comment')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 comment')


@given(u'Doesn\'t exist review at song "7 rings"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Doesn\'t exist review at song "7 rings"')


@when(u'I try to delete a review at song "7 rings"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I try to delete a review at song "7 rings"')


@then(u'I can not do it')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can not do it')
