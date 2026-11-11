from . import views
from django.urls import path

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("applications/", views.application_list, name="application_list"),
    path("employers/", views.employer_list, name="employer_list"),
    path("vacancies/", views.vacancy_list, name="vacancy_list"),

    path("vacancies/add/", views.VacancyCreateView.as_view(), name="vacancy_add"),
    path("vacancies/<int:pk>/edit/", views.VacancyUpdateView.as_view(), name="vacancy_edit"),
    path("vacancies/<int:pk>/delete/", views.VacancyDeleteView.as_view(), name="vacancy_delete"),

    path("employers/add/", views.EmployerCreateView.as_view(), name="employer_add"),
    path("employers/<int:pk>/edit/", views.EmployerUpdateView.as_view(), name="employer_edit"),
    path("employers/<int:pk>/delete/", views.EmployerDeleteView.as_view(), name="employer_delete"),

    path("applications/add/", views.ApplicationCreateView.as_view(), name="application_add"),
    path("applications/<int:pk>/edit/", views.ApplicationUpdateView.as_view(), name="application_edit"),
    path("applications/<int:pk>/delete/", views.ApplicationDeleteView.as_view(), name="application_delete"),
]
