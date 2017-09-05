```
      _      ___   ___  _
     | |    / _ \ / _ \| |
  ___| |__ | | | | | | | |_
 / __| '_ \| | | | | | | __|
 \__ \ | | | |_| | |_| | |_
 |___/_| |_|\___/ \___/ \__|
 

Integrated Testing Environment for Manual Security Testers
```


#### Features:
- Smart suggest test cases from various testing methodologies, Web Application Hacker's Handbook, OWASP Testing guide etc. You will never forget to test ***that***.
- Flow: Suggest Test case -> Confirm the bug -> Report
- Manage your own bug templates and auto prepare bug report from template.
- Handle multiple Assessments and Projects
- Never loose any data - Everything's saved automatically
- Integration with ServiceNow, JIRA (WIP)
- Export bug report into Markdown (WIP)
- Customize everything under-the-hood



#### Installation:
**Optional:** Set up [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and change the source: `source env/bin/activate`

**[Pip](https://pypi.python.org/pypi/pip):**
* Clone the latest version: `git clone https://github.com/pavanw3b/sh00t.git
`
* Navigate to the folder: `cd sh00t`
* Windows: `C:\Python27\python.exe -m pip install -r requirements.txt`
* Mac/Linux: `pip install -r requirements.txt --user`
* Setup database: `python manage.py migrate`
* Create User Account: `python manage.py createsuperuser` and follow the UI to create an user account as you like.
* Start Server: `python manage.py runserver`
* Hit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Stop the server: `Ctrl + C` to stop the Django server

#### Upgrade:
* Navigate to the folder where sh00t was cloned
* Stop the server if it's running: `Ctrl + C`
* Pull the latest code base: `git pull`
* Navigate to sh00t directory: `cd sh00t`
* \[Optional\]: If virtual environment is used, change the source: source env/bin/activate
* Make the latest database changes: `python manage.py migrate`
* Start: `python manage.py runserver`

### Troubleshoot:
Sh00t is powered by Django Web Framework. If you are stuck with any errors, Googling on the error message, should help you most of the times. If you are not sure, please [file a new issue on github](https://github.com/pavanw3b/sh00t/issues/new).

**Contribution:**
- Pavan: [@pavanw3b](https://twitter.com/pavanw3b)
- Aditya Ganapathy

**Credits:**
- Hari Valugonda
- Mohd Aqeel Ahmed
- Ajeeth Rakkappan
