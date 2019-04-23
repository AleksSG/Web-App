from .settings import *
import django_heroku

# IMPORTANT: to enable these settings in Heroku, set the corresponding environment variable using:
# $> heroku config:set DJANGO_SETTINGS_MODULE=MML.settings_heroku

DEBUG = False

ALLOWED_HOSTS = ['fast-reaches-35068.herokuapp.com']

# Configure Django App for Heroku.
django_heroku.settings(locals())