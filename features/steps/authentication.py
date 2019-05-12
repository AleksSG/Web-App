from behave import *
import splinter

use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
#    from django.contrib.auth.models import User
#    from MediaApp import UserProfileInfo

    #UserProfileInfo.objects.create_user(userne=username, email='usuari@usuari.com', password=password)
    print("hey")

@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/user_login'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('usuari', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()


#@given(u'a superuser "super" with password "superpass"')
#def step_impl(context):
    #print("Hooolaa")

@given('I\'m not logged in')
def step_impl(context):
    context.browser.form.find_by_value('Logout').first.click()
    assert context.browser.is_text_present('Login')

@then("I'm redirected to the login form")
def step_impl(context):
    context.browser.form.find_by_value('Login').first.click()
    assert context.browser.is_text_present('Login here')
