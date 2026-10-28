# Job Progression Management System
 
## Purpose
Help authorised employment advisers record and manage job applications.
 
## Primary user
An authorised employment adviser.
 
## Functional requirements
FR1: Users can log in and log out.
FR2: Users can view saved job applications.
FR3: Users can add a job application.
FR4: Users can edit a job application.
FR5: Users can delete a record after confirmation.
FR6: Forms validate required information.
FR7: Users can search by employer or job title.
FR8: Records are stored in SQLite.
FR9: Important functions have automated tests.
 
## Non-functional requirements
- Usability: pages and actions are easy to understand.
- Security: unauthenticated visitors cannot access protected pages.
- Maintainability: code is organised into Django files.
- Reliability: valid records save and can be retrieved.
 
## Acceptance criteria
- Valid credentials allow login.
- Invalid credentials are rejected.
- Valid records can be created, viewed, edited and deleted.
- Missing required data produces a validation message.
- Automated tests run and results are recorded.
 
## Limitations
This is a prototype. Advanced reporting, notifications and complex permissions are outside the initial scope.
