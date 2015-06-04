#!/bin/bash
# Script is called inside repo_name
# Create venv with python 3
pyvenv venv
# Activate venv
. venv/bin/activate
# Install requirements
pip install --upgrade pip
pip install --upgrade -r requirements/dev.txt
# Init git repo
git init
echo "venv/" > .gitignore
