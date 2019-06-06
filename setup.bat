@echo off
where python >nul 2>&1 && (
  echo [INSTALL] Found Python3
  pip3 >nul 2>&1 && (
    echo [INSTALL] Found pip3
  ) || (
    echo [ERROR] pip3 is not available in PATH. Install pip3.
    pause
    exit /b
  )

  echo [INSTALL] Installing Virtualenv
  pip3 install -U pip virtualenv
  virtualenv -p python ./env
  .\env\Scripts\activate
  echo [INSTALL] Installing Requirements
  pip install -r requirements.txt
  echo [INSTALL] Setting up Database
  python manage.py makemigrations
  python manage.py migrate
  echo [INSTALL] Creating an user account for you
  python manage.py createsuperuser

  echo [INSTALL] Setup testcases from WAHH and OWASP Testing Methodologies
  python reset.py

  echo [INSTALL] Installation Completed

  echo [RUN] Starting Sh00t..
  python manage.py runserver

) || (
  echo [ERROR] python3 is not installed. Install Python3 and make it available to us!
)