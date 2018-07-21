```
      _      ___   ___  _
     | |    / _ \ / _ \| |
  ___| |__ | | | | | | | |_
 / __| '_ \| | | | | | | __|
 \__ \ | | | |_| | |_| | |_
 |___/_| |_|\___/ \___/ \__|
 

A open platform for manual bug hunters.

```

Sh00t
- is a task manager that makes sure you "check that thing".
- provides checklists with which you will never regret for forgetting to "test that thing".
- helps to easily handle custom bug templates that can be separated for your different needs.


### Features:
- Dynamic Task Manager to replace simple editors or task management tools that are NOT meant for Security
- Automated, customizable Security test-cases Checklist to replace Evernote, OneNote or other tools which are NOT meant for Security
- Manage custom bug templates for different purposes and automatically generate bug report
- Support multiple Assessments & Projects to logically separate your different needs
- Use like a paper - Everything's saved automatically
- Export auto generated bug report into Markdown & submit blindly on HackerOne! (WIP)
- Integration with JIRA, ServiceNow (WIP)
- Export bug report into Markdown (WIP)
- Customize everything under-the-hood


### Installation:
Sh00t requires Python 3 and a few more packages. The simplest way to set up Sh00t is using Conda Environments.

**Pre-requisite - One time setup:**
* Install the minimal version of Anaconda: [Miniconda](https://conda.io/miniconda.html) and follow 
the [installation instruction](https://conda.io/docs/user-guide/install/index.html). Remember to 
reload your bash profile or restart your terminal application to avail conda command.
* Create a new Python 3 environment: `conda create -n sh00t python=3.6`
* Activate *sh00t* environment: `conda activate sh00t`. If you see an error message like 
`CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.`, you have to manually enable conda command. Follow the instructions shown with the error message. You may have to reload your bash profile 
or restart your terminal. Try activating sh00t again: `conda activate sh00t`. You should be seeing `(sh00t) XXXX$` in 
your terminal.
* Clone or download the latest project into a location of your choice: `https://github.com/pavanw3b/sh00t`
* Navigate to the folder where sh00t is cloned or downloaded & extracted: `cd sh00t`. Note that this is outer-most 
*sh00t* directory in project files. Not *sh00t/sh00t*.
* Install Sh00t dependency packages: `pip install -r requirements.txt`
* Setup database: `python manage.py migrate`
* Create an User Account: `python manage.py createsuperuser` and follow the UI to create an 
account.

That's all for the first time. Follow the next steps whenever you want to start Sh00t.

**Starting Sh00t:**
* Activate sh00t environment if not on yet: `conda activate sh00t`
* Navigate to sh00t directory if not in already: `cd sh00t`
* Start Sh00t server: `python manage.py runserver`
* Access [http://127.0.0.1:8000/](http://127.0.0.1:8000/) on your favorite browser. Login with the user credentials 
created in the one-time setup above.
* Welcome to Sh00t!
* Once you are done, stop the server: `Ctrl + C`
* [Optional] Deactivate sh00t environment to continue with your other work: `conda deactivate`.

### Upgrade:
* Navigate to the folder where sh00t was cloned
* Stop the server if it's running: `Ctrl + C`
* Pull the latest code base via git: `git pull` or download the source from github and replace the files.
* Navigate to sh00t directory: `cd sh00t`
* Activate sh00t environment if not on yet: `conda activate sh00t`
* Make the latest database changes: `python manage.py migrate`
* Start the server: `python manage.py runserver`

### Troubleshoot:
Sh00t is written in Python and powered by Django Web Framework. If you are stuck with any errors, Googling on the error 
message, should help you most of the times. If you are not sure, please [file a new issue on github](https://github
.com/pavanw3b/sh00t/issues/new).

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
