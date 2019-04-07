@echo off
where python >nul 2>&1 && (
    .\env\Scripts\activate
    echo [SETUP] Applying database changes if any
    python manage.py migrate
    echo [SETUP] Upgraded
) || (
  echo [ERROR] python3 is not installed
)