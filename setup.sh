#!/bin/bash

if ! [ -x "$(command -v python3)" ]; then
  echo '[ERROR] python3 is not installed.' >&2
  exit 1
fi
echo '[INSTALL] Found Python3'

echo '[INSTALL] Installing Virtualenv'
python3 -m pip install virtualenv

echo '[INSTALL] Using Virtualenv'
virtualenv env -p python3
source env/bin/activate

echo '[INSTALL] Installing Requirements'
pip install -r requirements.txt

echo '[INSTALL] Setting up Database'
python manage.py makemigrations
python manage.py migrate

echo '[INSTALL] Creating an user account for you'
python manage.py createsuperuser

echo '[INSTALL] Setting up testcases from WAHH and OWASP Testing Methodologies'
python reset.py

echo '[INSTALL] Installation Completed'

echo '[RUN] Starting Sh00t..'
python manage.py runserver