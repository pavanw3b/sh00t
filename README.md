<img src="https://user-images.githubusercontent.com/11267537/43043618-29ab7286-8db5-11e8-9603-71b30596d047.png" width="250" />

```
A Testing Environment for Manual Security Testers
```

![](https://img.shields.io/github/issues/pavanw3b/sh00t.svg)
![](https://img.shields.io/github/forks/pavanw3b/sh00t.svg)
![](https://img.shields.io/github/stars/pavanw3b/sh00t.svg)
![](https://img.shields.io/github/license/pavanw3b/sh00t.svg)
[![Rawsec's CyberSecurity Inventory](https://inventory.rawsec.ml/img/badges/Rawsec-inventoried-FF5050_flat.svg)](https://inventory.rawsec.ml/tools.html#Sh00t)

Sh00t
- is a task manager to let you focus on performing security testing
- provides **To Do** checklists of test cases
- helps to create bug reports with customizable bug templates


### Features:
- Dynamic Task Manager to replace simple editors or task management tools that are NOT meant for Security
- Automated, customizable Security test-cases Checklist to replace Evernote, OneNote or other tools which are NOT meant for Security
- Manage custom bug templates for different purposes and automatically generate bug report
- Support multiple Assessments & Projects to logically separate your different needs
- Use like a paper - Everything's saved automatically
- Export auto generated bug report into Markdown & submit blindly on HackerOne! (WIP)
- Integration with JIRA, ServiceNow - Coming soon
- Export bug report into Markdown - Coming soon
- Customize everything under-the-hood


### Installation:
1. Get the latest the latest source: `https://github.com/pavanw3b/sh00t/`
Clone (requires `git` installed): `git clone https://github.com/pavanw3b/sh00t.git` or download the zip file
2. [Install Python3](https://www.python.org/downloads/) if not installed already. 
3. Run the setup:

Windows: `setup.bat`

Linux/Mac: `./setup.sh`

**Note:** You will be prompted to enter Username & Password of your choice. Remember the username and password entered at this step. You will need to login with these credentials when you use Sh00t.

The setup script will install `virtualenv`, an isolated python environment, create a new environment named `env`, install the required dependencies in the environment, create & setup the database, create an user account, create 174 Security Test Cases from OWASP Testing Guide (OTG) and Web Application Hackers Handbook (WAHH) and start the server.

3. Logon to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) on your favorite browser. Login with the user credentials your provided in the previous step. 

**Starting Sh00t later:**
1. Run:

Windows: `run.bat`

Linux/Mac: `run.sh`

2. Logon to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) on your favorite browser. Login with the user credentials your provided at the time installation. 

### Upgrade:
1. Stop the server if it's running: `Ctrl + C`
2. Navigate to the folder where Sh00t was set up: `cd sh00t`
3. Get the latest source code either with `git pull` or download and copy the files. Make sure not to delete `db.sqlite3` file when copying files manually. You will lose your data if the file is lost.
3. Run the upgrade script:

Windows: `upgrage.bat`
Linux/Mac: `upgrade.sh`

4. Start Sh00t:

Windows: `run.bat`

Linux: `run.sh`

Logon to or reload: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Troubleshoot:
Sh00t is written in Python and powered by Django Web Framework. If you are stuck with any errors, Googling on the error 
message, should help you most of the times. If you are not sure, please [file a new issue on github](https://github.com/pavanw3b/sh00t/issues/new).

### Glossary:
- **Flag:** A Flag is a target that is sh00ted at. It's a test case that needs to be tested. Flags are generated automatically based on the testing methodology chosen. The bug might or might not be found - but the goal is to aim and sh00t at it. Flag contains detailed steps for testing. If the bug is confirmed, then it's called a sh0t.
- **Sh0t:** Sh0ts are bugs. Typically Sh0t contain technical description of the bug, Affected Files/URLs, Steps To Reproduce and Fix Recommendation. Most of the contents of Sh0t is one-click generated and only the dynamic content like Affected Parameters, Steps has to be changed. Sh0ts can belong to Assessment.
- **Assessment:** Assessment is a testing assessment. It can be an assessment of an application, a program - up to the user the way wanted to manage. It's a part of project.
- **Project:** Project contains assessments. Project can be a logical separation of what you do. It can be different job, bug bounty, up to you to decide.

### How does it work?
Begin with creating a new Assessment. Choose what methodology you want to test with. Today there are 330 test cases, grouped into 86 Flags, belonging to 13 Modules which are created with reference to "Web Application Hacker's Handbook" Testing Methodology. Modules & Flags can be handpicked & customized. Once Assessments are created with the Flags, now the tester has to test them either manually, or semi automated with the help of scanners, tools or however it's required, mark it "Done" on completion. While performing assessment we often come with custom test cases that is specific to certain scenario in the application. A new Flag can be created easily at any point of time.

Whenever a Flag is confirmed to be a valid bug, a Sh0t can be created. One can choose a bug template that matches best, and sh00t will auto fill the bug report based on the template chosen.


### Screenshots:

#### Dashboard:

![dashboard](https://user-images.githubusercontent.com/11267537/43355841-9f6167e4-9281-11e8-87fe-761fa35ddc3c.png)

#### Working on a Flag:

![flag](https://user-images.githubusercontent.com/11267537/43355838-9ee99e58-9281-11e8-8724-b9e726fdc58d.png)


#### Choosing Methodology and Test Cases while creating a new Assessment:
![new-assessment](https://user-images.githubusercontent.com/11267537/43355840-9f3a3368-9281-11e8-8afd-0467a4ac00b4.png)

#### Filing a bug pre-filled with a template:

![new-sh0t-from-template](https://user-images.githubusercontent.com/11267537/43355839-9f117630-9281-11e8-8a33-a9b5babae698.png)


### Who can use Sh00t?
- Application Security Engineers: Pentesting & Vulnerability Assessments
- Bug bounty hunters
- Independent Security Researchers
- Blue team, developers who fix
- Anybody who wants to hack

### Implementation details:
- Language: Python 3
- Framework: Django Web Framework
- Dependencies: Django REST Framework, djnago-tables2: Managed by /requirements.txt
- UI: Bootstrap - Responsive



**Contribution:**
- Pavan: [@pavanw3b](https://twitter.com/pavanw3b)
- [Aditya Ganapathy](https://github.com/adityadev91)

**Credits:**
- Hari Valugonda
- Mohd Aqeel Ahmed
- Ajeeth Rakkappan
