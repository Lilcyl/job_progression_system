Employer (1) ───────< Vacancy (many) ───────< JobApplication (many)
 
Employer fields:
name, email, phone, website, notes
 
Vacancy fields:
company (ForeignKey), position, salary, location, is_applied
 
JobApplication fields:
learner_name, learner_email, vacancy (ForeignKey),
application_date, status, notes
