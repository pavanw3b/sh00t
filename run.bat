@echo off
where python >nul 2>&1 && (
    .\env\Scripts\activate
    python manage.py runserver
) || (
  echo [ERROR] python3 is not installed
)