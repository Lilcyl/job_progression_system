
Job & Employability Progression Management System
A Django web application that lets authorised staff at a fictional employment and skills organisation record, find and manage job application information in one place, replacing scattered spreadsheets and documents.

Level 3 Software Development capstone project.

Purpose
Staff currently track vacancies, job applications, learner activity and progression across separate spreadsheets and documents. This prototype gives them a single, secure, searchable system for managing job application records.

Features
Staff login and logout; all pages protected from anonymous users
Staff and Administrator roles using Django groups and permissions
View a list of job applications
Add, edit and delete job applications
Search by learner, vacancy or employer, and filter by status
Input validation with clear messages (for example: blank name, future application date)
Success and error messages after actions
Django admin for managing employers and vacancies
Responsive Bootstrap 5 interface

Technologies
Area	Technology
Language	Python 3.10+
Framework	Django
Database	SQLite
Front end	Django templates, Bootstrap 5
Version control	Git and GitHub (Issues and Projects board)
Deployment	PythonAnywhere
Data model
Employer: name, sector, contact email
Vacancy: employer (FK), title, location, closing date, description
JobApplication: learner name, vacancy (FK), date applied, status, notes, created by (FK to User), created at
One Employer has many Vacancies; one Vacancy has many Job Applications; one User creates many Job Applications.

Installation
bash
git clone https://github.com/lilcyl/job_progession_system.git
cd job_progression_system

python -m venv venv
# Windows (PowerShell):  venv\Scripts\Activate.ps1
# Mac / Linux:           source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
Running locally
bash
python manage.py runserver
Open http://127.0.0.1:8000/ and log in. Use /admin/ to create the Staff and Administrators groups, users, employers and vacancies.

Optional environment variables
Variable	Purpose	Default (development only)
DJANGO_SECRET_KEY	Django secret key	insecure development key
DJANGO_DEBUG	True or False	True
DJANGO_ALLOWED_HOSTS	Comma-separated hosts	localhost,127.0.0.1
Never commit real secrets. .env and db.sqlite3 are listed in .gitignore.

Test procedure
Automated tests (models, forms, views, access control):

bash
python manage.py test -v 2
Manual tests are recorded in the test plan in docs/ (Test ID, requirement, steps, expected result, actual result, pass/fail, corrective action).

Project documentation
PROJECT_BRIEF.md: the employer brief, scope and requirements
ISSUES.md: planned GitHub Issues and priorities
docs/: requirements, design, test plan, defect log, security checklist, AI development journal, user guide, technical summary and reflection
Known limitations
No public registration or password-reset email; accounts are created by an administrator
SQLite suits a prototype, not heavy concurrent use
Basic search and no reporting or export
Fictional sample data only
Deployment
Deployed on PythonAnywhere: https://lilcyl.pythonanywhere.com

Summary of steps: clone the repository, create a virtual environment, pip install -r requirements.txt, set environment variables in the WSGI file, run migrate, createsuperuser and collectstatic, map /static/ to staticfiles/, then reload the web app.

Responsible AI use
AI tools were used as development assistants. All use is recorded in docs/ai-journal.md, and all submitted code was tested and is understood by the author.

Author
Ifeanyi Nwadioha, Level 3 Software Development Capstone


