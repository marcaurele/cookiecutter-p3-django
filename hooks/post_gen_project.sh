#!/bin/bash
# Script is called inside repo_name
# Create venv with python 3
pyvenv venv
# Activate venv
. venv/bin/activate
# Install requirements
pip install --upgrade pip
pip install --upgrade -r requirements/dev.txt
# Generate locale files in EN and FR
cd {{cookiecutter.pkg_name}}
django-admin makemessages -l en -l fr
# Init git repo
git init
echo "venv/" > .gitignore
