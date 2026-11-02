from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import JobApplication, Employer,Vacancy
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from . forms import EmployerForm, VacancyForm
from django.urls import reverse_lazy
#Create your views here.
# @login_required
# def application_list(request):
#     applications = JobApplication.objects.select_related(
#         "vacancy", "vacancy_company"
#     ).order_by("-application_date")

#     query = request.GET.get("q","").strip()
#     if query:
#         applications = applications.filter(
#             learner_name_icontains=query
#         ) | applications.filter(vacancy_company_name_icontains=query)
#     return render(
#         request,
#         "applications/application_list.html",
#         {"applications": applications, "query":query}
#     )

#protected views
@login_required
def dashboard(request):
    return render(request,"dashboard.html",{
        "employer_count": Employer.objects.count(),
        "vacancy_count": Vacancy.objects.count(),
        "application_count": JobApplication.objects.count
    })

@login_required
def employer_list(request):
    return render(request, "employers/list.html", {
        "employers":Employer.objects.all(),
    })

@login_required
def vacancy_list(request):
    return render(request, "vacancies/list.html", {
        "vacancies": Vacancy.objects.select_related("employer"),
    })

@login_required
def application_list(request):
    return render(request, "applications/list.html", {
        "applications": JobApplication.objects.select_related("vacancy", "vacancy_employer"),
    })
#protected views


#Employer views
class EmployerCreateView(LoginRequiredMixin, CreateView):
    model = Employer
    form_class = EmployerForm
    template_name = "employers/form.html"
    success_url = reverse_lazy("employer_list")

    def form_valid(self, form):
        messages.success(self.request, "Employer added successfully")
        return super().form_valid(form)

class EmployerUpdateView(LoginRequiredMixin, UpdateView):
    model = Employer
    form_class = EmployerForm
    template_name = "employers/form.html"
    success_url = reverse_lazy("employer_list")

class EmployerDeleteView(LoginRequiredMixin, DeleteView):
    model = Employer
    template_name = "employers/confirm_delete.html"
    success_url = reverse_lazy("employer_list")
#Employer views

#Vacancy views
class VacancyCreateView(LoginRequiredMixin, CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = "vacancies/form.html"
    success_url = reverse_lazy("vacancy_list")

    def form_valid(self, form):
        messages.success(self.request, "Vacancy added successfully")
        return super().form_valid

class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = "vacancies/form.html"
    success_url = reverse_lazy("vacancy_list")

class VacancyDeleteView(LoginRequiredMixin, DeleteView):
    model = Vacancy
    form_class = VacancyForm
    template_name = "vacancies/confirm_delete.html"
    success_url = reverse_lazy("vacancy_list")

# def application_list(request):
#     return HttpResponse("Books section of library")