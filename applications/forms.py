from django import forms
from .models import JobApplication, Vacancy, Employer

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ["name", "contact_person", "email", "phone", "website", "notes"]

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ["employer", "position", "salary", "location", "status"]

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "learner_name",
            "learner_email",
            "vacancy",
            "application_date",
            "status",
            "notes",
        ]

        widgets = {
            "application_date": forms.DateInput(format="%Y-%m-%d", attrs={"type":"date"}),
            "notes": forms.Textarea(attrs={"rows":3}),
        }