```
      _      ___   ___  _
     | |    / _ \ / _ \| |
  ___| |__ | | | | | | | |_
 / __| '_ \| | | | | | | __|
 \__ \ | | | |_| | |_| | |_
 |___/_| |_|\___/ \___/ \__|
 

A platform for application security testers that emphasises on manual security.

```

Sh00t
- is a task manager that makes sure you "check that thing".
- provides checklists with which you will never regret for forgetting to "test that thing".
- helps to easily handle custom bug templates that can be separated for your different needs.


#### Features:
- Dynamic Task Manager to replace simple editors or task management tools that are NOT meant for Security
- Automated, customizable Security test-cases Checklist to replace Evernote, OneNote or other tools which are NOT meant for Security
- Manage custom bug templates for different purposes and automatically generate bug report
- Support multiple Assessments & Projects to logically separate your different needs
- Use like a paper - Everything's saved automatically
- Export auto generated bug report into Markdown & submit blindly on HackerOne! (WIP)
- Integration with JIRA, ServiceNow (WIP)
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

### Glossary:
- **Flag:** A Flag is a target that is sh00ted at. It's a test case that needs to be tested. Flags are generated automatically based on the testing methodology chosen. The bug might or might not be found - but the goal is to aim and sh00t at it. Flag contains detailed steps for testing. If the bug is confirmed, then it's called a sh0t.
- **Sh0t:** Sh0ts are bugs. Typically Sh0t contain technical description of the bug, Affected Files/URLs, Steps To Reproduce and Fix Recommendation. Most of the contents of Sh0t is one-click generated and only the dynamic content like Affected Parameters, Steps has to be changed. Sh0ts can belong to Assessment.
- **Assessment:** Assessment is a testing assessment. It can be an assessment of an application, a program - up to the user the way wanted to manage. It's a part of project.
- **Project:** Project contains assessments. Project can be a logical separation of what you do. It can be different job, bug bounty, up to you to decide.

### How does it work?
Begin with creating a new Assessment. Choose what methodology you want to test with. Today there are 330 test cases, grouped into 86 Flags, belonging to 13 Modules which are created with reference to "Web Application Hacker's Handbook" Testing Methodology. Modules & Flags can be handpicked & customized. Once Assessments are created with the Flags, now the tester has to test them either manually, or semi automated with the help of scanners, tools or however it's required, mark it "Done" on completion. While performing assessment we often come with custom test cases that is specific to certain scenario in the application. A new Flag can be created easily at any point of time.

Whenever a Flag is confirmed to be a valid bug, a Sh0t can be created. One can choose a bug template that matches best, and sh00t will auto fill the bug report based on the template chosen.


### Screenshots:
![dashboard](https://user-images.githubusercontent.com/11267537/30522876-c8c77b8e-9bf4-11e7-8904-5a9bb9f0388f.png)
![flag](https://user-images.githubusercontent.com/11267537/30522877-c8cc5da2-9bf4-11e7-8014-eb8415ff6347.png)
![new-assessment](https://user-images.githubusercontent.com/11267537/30522878-c8cd0630-9bf4-11e7-8c9e-17d98aab4185.png)
![new-sh0t-from-template](https://user-images.githubusercontent.com/11267537/30522879-c8cdf888-9bf4-11e7-8fd4-228235e376e6.png)


### Who can use Sh00t?
- Application Security Engineers: Pentesting & Vulnerability Assessments
- Bug bounty hunters
- Independent Security Researchers
- Blue team, developers who fix
- Anybody who wants to hack

### Implementation details:
- Language: Python 2.7
- Framework: Django Web Framework
- Dependencies: Django REST Framework, TinyMCE (Managed by /requirements.txt)
- UI: Bootstrap - Responsive



**Contribution:**
- Pavan: [@pavanw3b](https://twitter.com/pavanw3b)
- [Aditya Ganapathy](https://github.com/adityadev91)

**Credits:**
- Hari Valugonda
- Mohd Aqeel Ahmed
- Ajeeth Rakkappan
