Cookiecutter Template for Django & Python 3
===========================================

A cookiecutter_ template for Django using Python 3.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Usage
-----
*The post generation hook script will not work on Windows.*::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/marcaurele/cookiecutter-p3-django.git

What's inside
-------------

The post hook will create a Python 3 virtual environment called ``venv`
and install these librairies (*versions have been explicitly not included
in the requirement files to download latest ones*):

- Django
- psycopg2
- pytz
- django-model-utils
- django-braces
- django-rosetta
- django-extensions
- django-debug-toolbar

Configurations
--------------

The production config file must be edited to set a couple of values.
