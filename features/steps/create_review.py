from behave import *
import splinter

use_step_matcher("parse")


@given(u'Exists a song')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists a song')


@when(u'I register a comment at the song "7 rings"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register a comment at the song "7 rings"')


@then(u'I\'m viewing the details page for song, the previous comments and the user\'s comment')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for song, the previous comments and the user\'s comment')


@then(u'There are 1 more comment than before')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 more comment than before')


@when(u'I register a new review at song "7 rings"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register a new review at song "7 rings"')


@then(u'There are 0 more comments than before')
def step_impl(context):
      raise NotImplementedError(u'STEP: When I register a new review at song "7 rings"')
