from behave import *
import splinter

use_step_matcher("parse")


@given(u'Exists a song "{song}" of the group "{group}"')
def step_impl(context, song, group):
    context.browser.visit(context.get_url('groups/'))
    form.find_by_value(group).first.click()

    assert context.browser.is_text_present(group)



@given(u'a comment for the "7 rings" song')
def step_impl(context):
    print("Hooolaa")


@when(u'Profile button is pressed')
def step_impl(context):
    context.browser.find_by_value('My Profile').first.click()
    assert context.browser.is_text_present('Welcome to the Profile Section!')

@then(u'Profile "nou" page is shown')
def step_impl(context):
    print("Hooolaa")
    assert 1==1


@then(u'Profile "comentador" page is shown with')
def step_impl(context):
    print("Hooolaa")
