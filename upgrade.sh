#!/bin/bash

if ! [ -x "$(command -v python3)" ]; then
  echo '[ERROR] python3 is not installed.' >&2
  exit 1
fi

source env/bin/activate

echo '[SETUP] Applying database changes if any'
python manage.py migrate

echo '[SETUP] Upgraded'