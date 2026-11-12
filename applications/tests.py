from django.test import TestCase
from datetime import timedelta
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils import timezone

from .forms import JobApplicationForm, VacancyForm
from .models import Employer, JobApplication, Vacancy

# Create your tests here.
User = get_user_model()


class JobProgressionTestData(TestCase):
    """Shared test data for the application tests."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="Test-password-123",
        )
        self.employer = Employer.objects.create(
            name="Northstar Technologies",
            email="jobs@northstar.example",
        )
        self.vacancy = Vacancy.objects.create(
            employer=self.employer,
            position="Python Developer",
            salary=Decimal("32000.00"),
            location="Leeds",
            status="Open",
        )
        self.application = JobApplication.objects.create(
            learner_name="Alex Morgan",
            learner_email="alex@example.com",
            vacancy=self.vacancy,
            application_date=timezone.localdate(),
            status="Applied",
        )


class EmployerModelTests(JobProgressionTestData):
    def test_employer_string_representation(self):
        self.assertEqual(str(self.employer), "Northstar Technologies")

    def test_employer_cannot_be_deleted_while_vacancies_exist(self):
        from django.db.models import ProtectedError

        with self.assertRaises(ProtectedError):
            self.employer.delete()


class VacancyModelTests(JobProgressionTestData):
    def test_vacancy_string_representation(self):
        self.assertEqual(
            str(self.vacancy),
            "Python Developer - Northstar Technologies",
        )

    def test_vacancy_is_linked_to_employer(self):
        self.assertEqual(self.vacancy.employer, self.employer)

    def test_negative_salary_is_invalid(self):
        vacancy = Vacancy(
            employer=self.employer,
            position="Tester",
            salary=Decimal("-1.00"),
        )
        with self.assertRaises(ValidationError):
            vacancy.full_clean()


class JobApplicationModelTests(JobProgressionTestData):
    def test_application_string_representation(self):
        self.assertEqual(
            str(self.application),
            "Alex Morgan - Python Developer",
        )

    def test_application_is_linked_to_vacancy(self):
        self.assertEqual(self.application.vacancy, self.vacancy)

    def test_application_date_defaults_to_today(self):
        application = JobApplication.objects.create(
            learner_name="Sam Taylor",
            vacancy=self.vacancy,
        )
        self.assertEqual(application.application_date, timezone.localdate())

    def test_future_application_date_is_invalid(self):
        application = JobApplication(
            learner_name="Sam Taylor",
            vacancy=self.vacancy,
            application_date=timezone.localdate() + timedelta(days=1),
        )
        with self.assertRaises(ValidationError):
            application.full_clean()


class JobApplicationFormTests(JobProgressionTestData):
    def test_valid_application_form(self):
        form = JobApplicationForm(data={
            "learner_name": "Jamie Lee",
            "learner_email": "jamie@example.com",
            "vacancy": self.vacancy.pk,
            "application_date": timezone.localdate().isoformat(),
            "status": "Applied",
            "notes": "Sent CV",
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_learner_name_is_required(self):
        form = JobApplicationForm(data={
            "learner_name": "",
            "learner_email": "",
            "vacancy": self.vacancy.pk,
            "application_date": timezone.localdate().isoformat(),
            "status": "Applied",
            "notes": "",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("learner_name", form.errors)

    def test_invalid_email_is_rejected(self):
        form = JobApplicationForm(data={
            "learner_name": "Jamie Lee",
            "learner_email": "not-an-email",
            "vacancy": self.vacancy.pk,
            "application_date": timezone.localdate().isoformat(),
            "status": "Applied",
            "notes": "",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("learner_email", form.errors)

    def test_future_application_date_is_rejected_by_form(self):
        form = JobApplicationForm(data={
            "learner_name": "Jamie Lee",
            "learner_email": "",
            "vacancy": self.vacancy.pk,
            "application_date": (
                timezone.localdate() + timedelta(days=1)
            ).isoformat(),
            "status": "Applied",
            "notes": "",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("application_date", form.errors)


class JobApplicationViewTests(JobProgressionTestData):
    def test_application_list_requires_login(self):
        response = self.client.get(reverse("application_list"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_logged_in_user_can_view_application_list(self):
        self.client.login(username="testuser", password="Test-password-123")
        response = self.client.get(reverse("application_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alex Morgan")

    def test_search_finds_learner_name(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("application_list"),
            {"q": "Alex Morgan"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alex Morgan")
        self.assertEqual(len(response.context["applications"]), 1)

    def test_search_finds_vacancy_position(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("application_list"),
            {"q": "Python Developer"},
        )
        self.assertEqual(len(response.context["applications"]), 1)

    def test_search_finds_employer_name(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("application_list"),
            {"q": "Northstar"},
        )
        self.assertEqual(len(response.context["applications"]), 1)

    def test_status_filter_returns_matching_applications(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("application_list"),
            {"status": "Applied"},
        )
        self.assertEqual(len(response.context["applications"]), 1)

    def test_search_and_status_filter_can_be_combined(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("application_list"),
            {"q": "Alex", "status": "Rejected"},
        )
        self.assertEqual(len(response.context["applications"]), 0)

    def test_search_with_no_matches_shows_empty_message(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("application_list"),
            {"q": "No matching learner"},
        )
        self.assertContains(response, "No job applications found")
        self.assertEqual(len(response.context["applications"]), 0)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_can_open_add_application_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("application_add"))
        self.assertEqual(response.status_code, 200)