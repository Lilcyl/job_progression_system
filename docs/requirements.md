# docs/requirements.md
 
# Job & Employability Progression Management System
 
## Purpose
A Django prototype that helps authorised employment advisers record employers,
vacancies and learner job applications.
 
## Primary user
An authorised employment adviser.
 
## Functional requirements
FR1: Users can log in and log out.
FR2: Authorised users can view employers.
FR3: Authorised users can add, edit and view employer details.
FR4: Authorised users can view vacancies and their employer.
FR5: Authorised users can add, edit and view vacancies.
FR6: Authorised users can record a learner's application to a vacancy.
FR7: Authorised users can update application status.
FR8: Users can delete records after a confirmation step where appropriate.
FR9: Forms validate required fields and show helpful errors.
FR10: Users can search or filter records where time permits.
 
## Non-functional requirements
- Usability: clear labels and navigation.
- Security: unauthenticated visitors cannot access protected pages.
- Reliability: saved records can be retrieved correctly.
- Maintainability: models, forms, views, URLs and templates are organised clearly.
 
## Acceptance criteria
- Valid login credentials allow access to protected pages.
- Invalid credentials are rejected.
- Employer, vacancy and application records can be created and viewed.
- Invalid or missing required information is not saved.
- An application displays the vacancy and the employer connected to it.
- Automated and manual tests are recorded.
