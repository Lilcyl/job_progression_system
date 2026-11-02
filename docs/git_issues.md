
GitHub Issues: Job & Employability Progression Management System
Copy each issue into Issues > New issue (title, labels, description). Then add them to the project board.

Suggested labels: must, should, could, setup, database, feature, security, ui, testing, documentation, deployment, bug

Board columns: Backlog, To Do, In Progress, In Review / Testing, Done

Suggested milestones: Day 1 Planning, Day 2 Core, Day 3 Access and UI, Day 4 Quality, Day 5 Delivery

Tip: put Closes #N in a commit message to close the issue automatically.

Issue 1: Set up development environment and Django project
Labels: must, setup | Milestone: Day 1 | Depends on: none

Create the local environment and a working Django project.

 Create project folder and virtual environment
 Install Django; create requirements.txt
 Create project config and app application
 Add application to INSTALLED_APPS; confirm SQLite
 Add .gitignore (venv, db.sqlite3, .env, staticfiles)
 First commit pushed; no sensitive files on GitHub
Acceptance criteria: python manage.py runserver shows the Django start page; repository contains no venv/ or db.sqlite3.

Issue 2: Create models: Employer, Vacancy, JobApplication
Labels: must, database | Milestone: Day 2 | Depends on: #1

 Define the three models with field types, choices and relationships
 Add model-level validation (no future application date)
 Run makemigrations; review output; run migrate
Acceptance criteria: tables exist; records can be created and retrieved in the Django shell; future date raises a validation error.

Issue 3: Register models in Django admin and add sample data
Labels: must, database | Milestone: Day 2 | Depends on: #2

 Register all models with useful list display, filters and search
 Create superuser
 Add 3 employers, 5 vacancies, 6 applications (fictional data only)
Acceptance criteria: all records visible and editable in /admin/; screenshots saved.

Issue 4: US2 Applications list page (FR3)
Labels: must, feature | Milestone: Day 2 | Depends on: #2

As an adviser, I want to see all job applications in a list so that I can review activity quickly.

 URL, view and template for list
 Show learner, employer, vacancy, date, status; newest first
 Friendly message when no records
Acceptance criteria: list shows all records in the correct order; empty state shows a message.

Issue 5: US3 Add application form with validation (FR5, FR9)
Labels: must, feature | Milestone: Day 2 | Depends on: #4

As an authorised adviser, I want to add a job application so that I can track a learner's employment activity.

 JobApplicationForm (ModelForm) with {% csrf_token %}
 Validate: name required (2+ characters), date not in the future, vacancy required
 Success message on save; errors shown under fields
Acceptance criteria: valid form saves and shows a success message; blank name or future date is rejected with a clear message and nothing is saved.

Issue 6: US4 Edit application (FR6)
Labels: must, feature | Milestone: Day 2 | Depends on: #5

 Edit view reusing the form; pre-filled values
 Success message
Acceptance criteria: changes save and appear in the list; invalid edits are rejected.

Issue 7: US5 Delete application with confirmation (FR7)
Labels: must, feature | Milestone: Day 2 | Depends on: #4

 Confirmation page before deletion
 Cancel returns without deleting
 Success message after deletion
Acceptance criteria: record is only removed after confirming; Cancel keeps it.

Issue 8: US1 Login and logout; protect views (FR1, FR2)
Labels: must, security | Milestone: Day 3 | Depends on: #4

 Use Django auth URLs and login template
 LOGIN_URL, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
 LoginRequiredMixin on every view
 Logout as a POST form with CSRF token
 Record logged-out and logged-in test evidence
Acceptance criteria: valid login opens the list; invalid login shows an error; protected URLs redirect to login when logged out, including typed-in URLs.

Issue 9: Staff and Administrator roles and permissions (FR7)
Labels: must, security | Milestone: Day 3 | Depends on: #7, #8

 Create Staff and Administrators groups with the right permissions
 Delete view requires tracker.delete_jobapplication (403 otherwise)
 Hide Delete button when user lacks permission
Acceptance criteria: staff user gets 403 on the delete URL; administrator can delete.

Issue 10: US6 Search and filter (FR8)
Labels: should, feature | Milestone: Day 2 | Depends on: #4

 Search by learner, vacancy or employer
 Filter by status
 Clear button and no-match message
Acceptance criteria: only matching records shown; no-match shows a clear message.

Issue 11: Base template and Bootstrap styling
Labels: should, ui | Milestone: Day 3 | Depends on: #4

 base.html with navigation and messages area; template inheritance for all pages
 Bootstrap 5; clear Add/Edit/Delete buttons
 Check at phone, tablet and desktop widths
Acceptance criteria: consistent layout on all pages; table scrolls rather than breaks on narrow screens.

Issue 12: Peer usability review and one improvement
Labels: should, ui, documentation | Milestone: Day 3 | Depends on: #11

 Another learner completes three tasks unaided
 Record feedback
 Implement at least one improvement
Acceptance criteria: feedback table complete; improvement committed with a message referencing the feedback.

Issue 13: Security review and checklist
Labels: must, security, documentation | Milestone: Day 3 | Depends on: #8, #9

 Confirm CSRF tokens in all POST forms
 No |safe or autoescape off on untrusted content
 Secret key, debug and allowed hosts read from environment
 No secrets or real personal data in the repository
 Complete docs/security-checklist.md
Acceptance criteria: every checklist item verified and ticked.

Issue 14: Create manual test plan
Labels: must, testing, documentation | Milestone: Day 4 | Depends on: #8

 Test table: ID, requirement, steps/input, expected, actual, pass/fail, corrective action
 Positive, negative, authentication, CRUD and validation tests
 At least one test per major requirement; run and record results with screenshots
Acceptance criteria: all functional requirements covered; failures have corrective actions and retests.

Issue 15: Automated Django tests
Labels: must, testing | Milestone: Day 4 | Depends on: #9

 Model, form, view and access-control tests
 Run suite; capture first and final results
 Investigate and fix failures
Acceptance criteria: python manage.py test passes; screenshots of first and final runs saved.

Issue 16: Maintain defect log
Labels: must, testing, documentation | Milestone: Day 4 | Depends on: none (ongoing)

 Each defect has ID, description, reproduction steps, cause, correction, retest, status
 Escalation note for any unresolved defect
Acceptance criteria: at least 5 entries, closed or with an escalation note.

Issue 17: Maintain AI Development Journal
Labels: must, documentation | Milestone: Day 4 | Depends on: none (ongoing)

 Entry per use: tool, prompt, response summary, why, accepted/modified/rejected, how tested
 One helpful use and one human correction
 Final responsible-AI reflection
Acceptance criteria: journal complete; all submitted code explainable.

Issue 18: GitHub quality review and final README
Labels: must, documentation | Milestone: Day 4 | Depends on: #15

 Review commit history and branches; merge approved work
 Close completed issues; remove unnecessary files; review .gitignore
 README covers purpose, features, technologies, installation, running, tests, limitations, deployment, author
Acceptance criteria: repository is tidy; README lets a new reader install and run the project.

Issue 19: Deploy to PythonAnywhere
Labels: must, deployment | Milestone: Day 5 | Depends on: #15, #13

 Clone repo, create virtualenv, install requirements
 Configure WSGI file and environment variables
 Run migrate, createsuperuser, collectstatic; map /static/
 Reload; test login, CRUD, forms and navigation
 Log and fix deployment defects; capture evidence with the address bar visible
Acceptance criteria: live site works for login and all CRUD operations.

Issue 20: User guide
Labels: must, documentation | Milestone: Day 5 | Depends on: #19

 Access, login, navigation, add, edit, delete
 Screenshots from the live site
 Troubleshooting table
Acceptance criteria: a new adviser could use the system from the guide alone.

Issue 21: Technical project summary
Labels: must, documentation | Milestone: Day 5 | Depends on: #19

 Problem, solution, stack, why SQLite, models, functionality, testing, security, Git/GitHub, AI use, limitations, future improvements
Acceptance criteria: all 12 headings covered.

Issue 22: Final portfolio check
Labels: must, documentation | Milestone: Day 5 | Depends on: #20, #21

 Tick every evidence item; check filenames, readability and duplicates
 Screenshots show behaviour, not just code
Acceptance criteria: checklist complete; every major part can be explained.

Issue 23: Demonstration
Labels: must, documentation | Milestone: Day 5 | Depends on: #22

 Script: problem, solution, login, create, view, update, delete, validation/security, testing, GitHub, challenge, AI use, limitation, improvement
 Rehearse to 5 to 7 minutes; prepare answers to likely questions
Acceptance criteria: demo runs to time using the live site, with a local backup ready.

Issue 24: Final learner reflection
Labels: must, documentation | Milestone: Day 5 | Depends on: none

 Cover all 12 reflection prompts from the brief
Acceptance criteria: specific, honest examples under each prompt.

Optional (Could have)
Issue 25: Pagination on the list page
Labels: could, feature | Depends on: #4

Issue 26: Export applications to CSV
Labels: could, feature | Depends on: #4

Issue 27: Dashboard counts by status
Labels: could, feature | Depends on: #4

Optional: create the issues from the command line
If you have the GitHub CLI installed and signed in (gh auth login), run this inside your cloned repository to create the labels and a few issues. Repeat the gh issue create line for the rest.

bash
for l in must should could setup database feature security ui testing documentation deployment bug; do
  gh label create "$l" --force
done

gh issue create --title "Set up development environment and Django project" \
  --label must,setup --body "Create venv, install Django, create project config and app tracker, add .gitignore, first push."

gh issue create --title "Create models: Employer, Vacancy, JobApplication" \
  --label must,database --body "Define models, validation, makemigrations, migrate. Depends on #1."

Claude finished the response
