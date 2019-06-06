#!/bin/bash

if ! [ -x "$(command -v python3)" ]; then
  echo '[ERROR] python3 is not installed.' >&2
  exit 1
fi
echo '[INSTALL] Found Python3'

command
status=$?
cmd="python3 -m pip -V"
$cmd
status=$?
if [ $status -eq 0 ]; then
  echo "[INSTALL] Found pip"
  python3 -m pip install --upgrade pip
else
  echo "[ERROR] The command ($cmd) failed. python3-pip not installed"
  exit 1
fi

echo '[INSTALL] Installing Virtualenv'
python3 -m pip install virtualenv --user

echo '[INSTALL] Using Virtualenv'
python3 -m pip virtualenv env -p python3
source env/bin/activate

echo '[INSTALL] Installing Requirements'
pip install -r requirements.txt

echo '[INSTALL] Setting up Database'
python3 manage.py makemigrations
python3 manage.py migrate

echo '[INSTALL] Creating an user account for you'
python3 manage.py createsuperuser

echo '[INSTALL] Setting up testcases from WAHH and OWASP Testing Methodologies'
python3 reset.py

echo '[INSTALL] Installation Completed'

echo '[RUN] Starting Sh00t..'
python3 manage.py runserver