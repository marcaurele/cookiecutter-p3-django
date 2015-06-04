# -*- coding: utf-8 -*-

from .base import *

# SECRET
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY')

# ------------------------------------------------------------------------------
# --------------- SECTION BELOW MUST BE EDITED ---------------------------------
# ------------------------------------------------------------------------------

# SITE
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# DATABASE
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# MAIL
# ------------------------------------------------------------------------------
DEFAULT_EMAIL_FROM = '{{cookiecutter.project_name}} <noreply@peakxl.ch>'
EMAIL_SUBJECT_PREFIX = '[{{cookiecutter.project_name}}] '
EMAIL_HOST = env('DJANGO_EMAIL_HOST')
EMAIL_PORT = env('DJANGO_EMAIL_PORT')
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# FILES/MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = '/var/www/example.com/media/'
MEDIA_URL = '//bits.dommain.ch/files/'
STATIC_ROOT = '/var/www/example.com/static/'
STATIC_URL = '//bits.domain.ch/static/'
STATICFILES_DIRS = (
    os.path.join(SITE_DIR, 'static'),
)
