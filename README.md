# Job & Employability Progression Management System

A Django web application and FastAPI REST API for managing employers, job vacancies and learner job applications.

**Project level:** Level 3 Software Development Capstone  
**Database:** SQLite  
**Version control:** Git and GitHub

---

## 1. Project Overview

The Job & Employability Progression Management System is designed to help staff at a fictional employment and skills organisation manage job opportunities and learner employment progression.

Organisations may use separate spreadsheets and documents to record employer details, vacancies and learner applications. This can make information difficult to find, update and maintain.

This project provides a centralised system where authorised staff can record, search, view, update and delete information about employers, vacancies and job applications.

The project contains two main components:

1. **Django web application** – provides the user interface for managing records.
2. **FastAPI REST API** – provides endpoints for accessing and managing the same database programmatically.

Both components are designed to work with the same SQLite database.

## 2. Project Objectives

The main objectives are to:

- Create a central database for employer, vacancy and application records.
- Allow authorised staff to manage records through a web interface.
- Provide search and filtering functionality.
- Validate information before it is saved.
- Protect application pages using authentication.
- Provide a REST API for external access to the system.
- Apply database relationships to reduce duplicate information.
- Use automated testing to check that the application behaves as expected.
- Use Git and GitHub to manage source code and project development.

## 3. Main Features

### Django Web Application

| Feature | Description |
|---|---|
| User authentication | Staff can log in and log out. |
| Dashboard | Displays the number of employers, vacancies and applications. |
| Employer management | Add, view, edit and delete employer records. |
| Vacancy management | Add, view, edit and delete job vacancies. |
| Application management | Add, view, edit and delete job applications. |
| Search | Search applications by learner name, vacancy position or employer name. |
| Status filtering | Filter applications by their current status. |
| Form validation | Validate submitted information before saving. |
| Access protection | Require users to log in before accessing protected pages. |
| Django admin | Manage database records through the administration interface. |

### FastAPI REST API

The API provides programmatic access to the project database.

| Resource | Available operations |
|---|---|
| Employers | Create, read, update and delete employers. |
| Vacancies | Create, read, update and delete vacancies. |
| Applications | Create, read, update, delete, search and update application status. |
| Statistics | Retrieve employer, vacancy and application totals. |
| Health | Check whether the API service is running. |

The API uses Pydantic schemas to validate incoming and outgoing data and SQLAlchemy to communicate with the database.

## 4. Technologies Used

| Area | Technology |
|---|---|
| Programming language | Python |
| Web framework | Django |
| API framework | FastAPI |
| Database | SQLite |
| Django database access | Django ORM |
| API database access | SQLAlchemy |
| API data validation | Pydantic |
| Frontend | HTML, CSS and Bootstrap 5 |
| API testing | FastAPI TestClient and HTTPX |
| Automated testing | Django Test Framework and Pytest |
| Environment configuration | python-dotenv |
| Version control | Git and GitHub |
| Deployment | PythonAnywhere for the Django web application |

## 5. Project Structure

The main project files are organised as follows:

```text
job_progression_system/
│
├── api/
│   ├── routers/
│   │   ├── applicationsRouter.py
│   │   ├── employersRouter.py
│   │   ├── vacanciesRouter.py
│   │   └── stats.py
│   │
│   ├── tests/
│   │   ├── conftest.py
│   │   └── test_api.py
│   │
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
│
├── applications/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── docs/
│   ├── 01_project_brief.md
│   ├── git_issues.md
│   ├── relationship_diagram.md
│   ├── requirements.md
│   ├── user_stories.md
│   └── screenshots/
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## 6. Database Design

The system contains three main database entities.

### Employer

Stores information about organisations that provide job opportunities.

Fields include:

- `id` – unique employer identifier.
- `name` – employer name.
- `contact_person` – employer contact person.
- `email` – employer email address.
- `phone` – employer telephone number.
- `website` – employer website.
- `notes` – additional information.

### Vacancy

Stores information about available job opportunities.

Fields include:

- `id` – unique vacancy identifier.
- `employer` – foreign key linking the vacancy to an employer.
- `position` – job title or position.
- `salary` – vacancy salary.
- `location` – job location.
- `status` – whether the vacancy is Open or Closed.

### JobApplication

Stores information about learners applying for vacancies.

Fields include:

- `id` – unique application identifier.
- `learner_name` – learner's name.
- `learner_email` – learner's email address.
- `vacancy` – foreign key linking the application to a vacancy.
- `application_date` – date of application.
- `status` – current application status.
- `notes` – additional application information.

### Database Relationships

- One Employer can have many Vacancies.
- Each Vacancy belongs to one Employer.
- One Vacancy can have many Job Applications.
- Each Job Application belongs to one Vacancy.

The relationships are implemented using Django foreign keys and SQLAlchemy relationships.

For more information, see [docs/relationship_diagram.md](docs/relationship_diagram.md).

## 7. Application Statuses

Job applications can have the following statuses:

| Status | Meaning |
|---|---|
| Draft | Application information has been recorded but is not yet submitted. |
| Applied | The learner has submitted an application. |
| Interview | The learner has been invited to an interview. |
| Rejected | The application was unsuccessful. |
| Offer | The learner has received a job offer. |
| Withdrawn | The learner has withdrawn the application. |

Vacancies can have two statuses:

- Open
- Closed

## 8. Installation and Setup

Follow these instructions to run the project locally.

### Step 1: Clone the repository

```bash
git clone https://github.com/Lilcyl/job_progression_system.git

cd job_progression_system
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

Activate the environment.

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

Install the testing dependencies if they are not already included:

```bash
pip install pytest pytest-cov
```

### Step 4: Configure environment variables

Create a `.env` file in the project root.

Example development configuration:

```text
DJANGO_SECRET_KEY=replace-with-a-secure-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
API_KEY=replace-with-a-secure-api-key
```

Use secure, unique values for the secret key and API key.

Do not commit the `.env` file or real credentials to GitHub.

### Step 5: Apply database migrations

```bash
python manage.py migrate
```

This creates or updates the database tables required by Django.

### Step 6: Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the instructions to create your administrator username and password.

### Step 7: Start the Django application

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

The Django administration interface is available at:

http://127.0.0.1:8000/admin/

## 9. Running the FastAPI Application

The FastAPI application provides a separate API service.

Start it from the project root:

```bash
uvicorn api.main:app --reload --port 8001
```

The API service will be available at:

http://127.0.0.1:8001/

### API documentation

FastAPI automatically provides interactive API documentation.

Open:

http://127.0.0.1:8001/docs

You can use this page to explore endpoints and submit API requests.

### API authentication

Protected API endpoints require an API key.

The key must be sent using the `X-API-Key` request header.

Example:

```text
X-API-Key: your-api-key
```

The API key must match the `API_KEY` environment variable configured on the server.

The health endpoint (`/health`) is public and does not require an API key.

## 10. API Endpoints

The following table describes the intended API routes.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API availability. |
| GET | `/employers` | Retrieve employers. |
| POST | `/employers` | Create an employer. |
| GET | `/employers/{employer_id}` | Retrieve one employer. |
| PUT | `/employers/{employer_id}` | Update an employer. |
| DELETE | `/employers/{employer_id}` | Delete an employer. |
| GET | `/vacancies` | Retrieve vacancies. |
| POST | `/vacancies` | Create a vacancy. |
| GET | `/vacancies/{vacancy_id}` | Retrieve one vacancy. |
| PUT | `/vacancies/{vacancy_id}` | Update a vacancy. |
| DELETE | `/vacancies/{vacancy_id}` | Delete a vacancy. |
| GET | `/applications` | Retrieve and search applications. |
| POST | `/applications` | Create an application. |
| GET | `/applications/{application_id}` | Retrieve one application. |
| PUT | `/applications/{application_id}` | Update an application. |
| PATCH | `/applications/{application_id}/status` | Update application status. |
| DELETE | `/applications/{application_id}` | Delete an application. |
| GET | `/stats` | Retrieve system statistics. |

### Search and filtering examples

Search applications by learner, vacancy or employer:

```text
GET /applications?q=Python
```

Filter applications by status:

```text
GET /applications?status=Interview
```

Filter applications by vacancy:

```text
GET /applications?vacancy_id=1
```

Retrieve vacancies by status:

```text
GET /vacancies?status=Open
```

Retrieve vacancies by employer:

```text
GET /vacancies?employer_id=1
```

The API also supports pagination using `skip` and `limit` query parameters on its list endpoints.

## 11. Validation and Error Handling

The system uses validation to help maintain accurate records.

Examples include:

- Employer names must be provided.
- Vacancy positions must be provided.
- Vacancy salaries cannot be negative.
- Application learner names must be valid.
- Application dates cannot be in the future.
- Application statuses must match the available choices.
- A vacancy must reference an existing employer.
- An application must reference an existing vacancy.

The system also uses protected foreign key relationships to prevent deleting employers or vacancies that still have dependent records.

The API returns appropriate HTTP status codes for successful requests and errors, including:

| Status code | Meaning |
|---|---|
| 200 | Request successful. |
| 201 | Record created successfully. |
| 204 | Record deleted successfully. |
| 401 | API key missing or invalid. |
| 404 | Requested record not found. |
| 409 | Record cannot be deleted because dependent records exist. |
| 422 | Submitted information failed validation. |
| 500 | Server configuration or internal error. |

## 12. Automated Testing

The project contains Django tests and FastAPI API tests.

### Run Django tests

```bash
python manage.py test
```

Run with additional detail:

```bash
python manage.py test -v 2
```

### Run FastAPI tests

```bash
pytest api/tests -v
```

### Run API tests with coverage

```bash
pytest api/tests --cov=api
```

### What should be tested?

The tests should cover:

- Model creation and relationships.
- Form validation.
- Application search and filtering.
- Login and access protection.
- Employer, vacancy and application CRUD operations.
- API authentication.
- Invalid or missing data.
- Missing database records.
- Application status updates.
- Database relationship protection.
- API statistics.

Tests should be executed after changes are made to ensure that existing functionality has not been broken.

## 13. Version Control

Git is used to track changes to the project.

Example commands:

Check modified files:

```bash
git status
```

Add files:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Describe your changes"
```

Push commits to GitHub:

```bash
git push origin main
```

It is good practice to make small, meaningful commits and test your changes before pushing them.

Never commit passwords, API keys, secret keys, private database files or other sensitive information.

## 14. Deployment

The Django web application has a PythonAnywhere deployment reference:

https://lilcyl.pythonanywhere.com

The deployment process generally involves:

1. Uploading or cloning the project.
2. Creating and activating a virtual environment.
3. Installing the required dependencies.
4. Configuring environment variables securely.
5. Applying database migrations.
6. Configuring the WSGI application.
7. Configuring static files.
8. Reloading the web application.
9. Testing the deployed application.

The FastAPI service requires its own ASGI-capable deployment configuration. Its deployment should be documented separately if it is hosted independently.

## 15. Known Limitations

This project is a learning and prototype system. Some limitations include:

- SQLite is suitable for development and small-scale use but may not be ideal for a larger organisation.
- The system does not currently provide a full reporting and export facility.
- There is no public user registration.
- Password reset emails require additional email server configuration.
- The API and Django application need to remain consistent when database models change.
- The API service requires separate hosting and configuration if deployed independently.
- The project uses fictional employer and learner information for demonstration purposes.

## 16. Future Improvements

Possible improvements include:

- Add pagination to the Django application list.
- Add more advanced dashboard reporting.
- Add CSV and Excel export.
- Improve user roles and permissions.
- Add password reset functionality.
- Add automated API integration tests against the shared database.
- Add more detailed audit logging.
- Introduce a production database such as PostgreSQL.
- Add automated deployment and continuous integration.
- Improve API documentation and error responses.

## 17. Responsible Use of AI

AI tools may be used to support development activities such as:

- Explaining programming concepts.
- Suggesting code improvements.
- Drafting documentation.
- Identifying possible errors.
- Suggesting test cases.

AI-generated code and documentation must be reviewed and understood before use.

Developers remain responsible for executing tests, checking results, protecting sensitive information and ensuring that the final work meets the project requirements.

## 18. Author

**Author:** Ifeanyi Nwadioha  
**Project:** Job & Employability Progression Management System  
**Level:** Level 3 Software Development Capstone

---

*This README describes the intended project structure and functionality. Verify the installation, API startup and tests against the current code before treating the documented features as fully operational.*