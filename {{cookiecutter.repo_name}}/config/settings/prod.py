# -*- coding: utf-8 -*-

from .base import *

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY')

# ------------------------------------------------------------------------------
# --------------- SECTION BELOW MUST BE EDITED ---------------------------------
# ------------------------------------------------------------------------------

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]


# COOKIES - Removed if using SSL, which you should in production
# ------------------------------------------------------------------------------
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


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


# Mail settings
# ------------------------------------------------------------------------------
DEFAULT_EMAIL_FROM = 'PeakXL <noreply@peakxl.ch>'
EMAIL_SUBJECT_PREFIX = '[{{cookiecutter.project_name}}] '
EMAIL_HOST = env('DJANGO_EMAIL_HOST')
EMAIL_PORT = env('DJANGO_EMAIL_PORT')
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
#MEDIA_ROOT = os.path.join(SITE_DIR, 'files')
MEDIA_ROOT = '/var/www/example.com/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '//bits.dommain.ch/files/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/var/www/example.com/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '//bits.domain.ch/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_DIR, 'static'),
)
