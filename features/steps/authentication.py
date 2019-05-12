from behave import *


use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}", email "{email}" and birthday {bday}')
def step_impl(context, username, password, email, bday):
    from django.contrib.auth.models import User
    from MediaApp.models import UserProfileInfo
    us = User.objects.create_user(username=username, email=email, password=password)
    user = UserProfileInfo(us,bday)

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    from MediaApp.models import UserProfileInfo
    us = User.objects.create_user(username=username, email=None, password=password)
    user = UserProfileInfo(us,None)

@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/user_login'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()


@given(u'There is not user "user" registred')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given There is not user "user" registred')
