# Project Brief: Job & Employability Progression Management System

## 1. Title

Design, Develop, Test and Deploy a Full-Stack Workplace Application

## 2. Objective

Bring together the knowledge, skills and behaviours from the programme by planning, building, testing, documenting, version-controlling, deploying and demonstrating a complete but appropriately scoped Python/Django application.

## 3. Context

A fictional employment and skills organisation supports jobseekers through training and employment progression. Staff currently use separate spreadsheets and documents to record vacancies, job applications, learner activity and progression. The organisation wants a prototype web application that lets authorised users record and manage job application information.

## 4. Business problem

Job application information is scattered across spreadsheets and documents, so it is duplicated, hard to search, easy to get out of date, and not protected by proper access control.

## 5. Proposed solution

A staff-only Django web application backed by SQLite that holds employers, vacancies and job applications in one database, with login, CRUD, search, validation and role-based permissions.

## 6. Users

| User | Needs | Access |
|---|---|---|
| Adviser / Staff (primary) | Record, update and search job applications | Log in; view, add, edit |
| Administrator | All staff abilities, plus deleting records and managing users and reference data | Log in; view, add, edit, delete; Django admin |
| Visitor (not logged in) | None | Redirected to login |

## 7. Information to manage

- Employers
- Vacancies
- Job applications (the core record)
- Staff user accounts

## 8. Technical requirements (from the brief)

- Django web application with SQLite
- User authentication
- Database-driven CRUD functionality
- Validation
- Testing
- Git/GitHub source control, with GitHub as the authoritative repository
- Appropriate documentation
- PythonAnywhere deployment where suitable
- AI tools allowed as assistants, with evidence of use; all code must be understood, tested and explainable

## 9. Scope (MoSCoW)

| Priority | Items |
|---|---|
| **Must have** | Login/logout; list, add, edit and delete applications (with delete confirmation); input validation; Employer and Vacancy records; automated tests; GitHub; deployment |
| **Should have** | Search and status filter; detail page; success/error messages; Staff and Administrator roles; Bootstrap styling |
| **Could have** | Pagination; CSV export; dashboard counts; learner profile table; email reminders |
| **Won't have** | Public registration; payments; real email sending; complex analytics |

## 10. Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR1 | Users can log in with a username and password and log out | Must |
| FR2 | Only logged-in users can view or change records | Must |
| FR3 | List all job applications (learner, employer, vacancy, date, status) | Must |
| FR4 | Detail page for a single job application | Should |
| FR5 | Add a job application using a validated form | Must |
| FR6 | Edit an existing job application | Must |
| FR7 | Authorised users can delete an application after a confirmation step | Must |
| FR8 | Search by learner, vacancy or employer; filter by status | Should |
| FR9 | Invalid input is rejected with clear messages | Must |
| FR10 | Administrators manage employers and vacancies via the admin site | Should |

## 11. Non-functional requirements

- **Usability:** consistent navigation, clearly labelled actions, works on phone and desktop widths
- **Security:** Django authentication, CSRF protection, server-side permission checks, no secrets in GitHub, no real personal data
- **Maintainability:** one clearly organised app, meaningful commits, automated tests
- **Reliability:** data validated before saving to SQLite

## 12. Example user stories

- As an authorised adviser, I want to add a job application so that I can track a learner's employment activity.
- As an adviser, I want to search and filter applications so that I can find a record quickly.
- As an administrator, I want to delete an application after confirming so that mistakes can be removed safely.

## 13. Data design

- **Employer:** name (unique), sector, contact email
- **Vacancy:** employer (FK), title, location, closing date, description
- **JobApplication:** learner name, vacancy (FK), date applied, status, notes, created by (FK to User), created at

Status choices: Applied, Shortlisted, Interview, Offered, Rejected, Withdrawn.

Validation: learner name required (at least 2 characters), application date not in the future, vacancy required, status from the list, employer name unique.

## 14. Delivery phases

1. Understand the brief
2. Requirements and user stories
3. Plan in GitHub
4. Design the application
5. Development environment
6. Build the database
7. Core CRUD
8. Authentication and access control
9. User interface
10. Basic security
11. Test plan
12. Automated Django testing
13. Defect management
14. Responsible AI-assisted development
15. GitHub quality review
16. Deployment
17. User guide
18. Technical project summary
19. Final portfolio check
20. Demonstration
21. Final reflection

## 15. Portfolio evidence

Requirements, user stories, acceptance criteria, planning evidence, wireframes, database/model design, source code, GitHub repository, commit history, issues/project-board evidence, screenshots, test plan, automated tests, test results, defect log, security checklist, AI Development Journal, README, user guide, deployment evidence, reflection.

## 16. Decision log

| ID | Decision | Reason |
|---|---|---|
| D1 | Project name: Job & Employability Progression Management System | Recommended in the brief |
| D2 | Staff-only access; no public registration | Brief specifies authorised users |
| D3 | Job Application is the core record | Main thing staff track |
| D4 | Separate Staff and Administrator roles | Confirmed with supervisor |
| D5 | One Django app called `tracker` | Keeps scope simple |
| D6 | Deploy to PythonAnywhere only where suitable | Per brief and supervisor |

## 17. Success criteria

The finished project gives a coherent evidence trail from employer requirement, planning, design, development, Git/GitHub, testing, debugging, security, deployment, documentation and demonstration through to reflection, with a working, deployed, tested application the learner can fully explain.