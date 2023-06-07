#!/bin/bash

# This script creatings a whole new project by:
# 1º - Creating a virtualenv
# 2º - Installing all packages listed in "packages.txt"
# 3º - Setting up the packages


# 1̣º - CREATING THE VENV
# Create the virtual environment
python3 -m virtualenv venv

# Activate the virtual environment
source venv/bin/activate


# 2º - INSTALLING THE LISTED PACKAGES
# Install the packages from "requirements.txt" file
pip install -r requirements.txt


# 3º - SETTING UP THE PACKAGES

# # 3.1º - pre-commit
# Installing pre-commit
pre-commit install
