# -*- coding: utf-8 -*-
"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

def env(var_name, default=None):
    """
    To retrieve vars from environment variables. 
    """
    if var_name in os.environ:
        return os.environ[var_name]
    elif default is not None:
        return default
    else:
        raise ImproperlyConfigured(
            "Set the %s environment variable" % var_name)

BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
    '..', '..')
SITE_DIR = os.path.join(BASE_DIR, 'site')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Application definition
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
THIRD_PARTY_APPS = ()
LOCAL_APPS = ()
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = '{{cookiecutter.timezone}}'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# LOCALES
# ------------------------------------------------------------------------------
from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# EXTRA SETTINGS
# ------------------------------------------------------------------------------
ADMINS = (
    ('{{cookiecutter.full_name}}', '{{cookiecutter.email}}'),
)
MANAGERS = ADMINS