from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import JobApplication, Employer,Vacancy
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from . forms import EmployerForm, VacancyForm, JobApplicationForm
from django.urls import reverse_lazy

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
    return render(request, "applications/application_list.html", {
        "applications": JobApplication.objects.select_related("vacancy"),
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
        return super().form_valid(form)

class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = "vacancies/form.html"
    success_url = reverse_lazy("vacancy_list")
    

class VacancyDeleteView(LoginRequiredMixin, DeleteView):
    model = Vacancy
    template_name = "vacancies/confirm_delete.html"
    success_url = reverse_lazy("vacancy_list")
#Vacancy Views End

#Job Application Views
class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = "applications/form.html"
    success_url = reverse_lazy("application_list")

    def form_valid(self, form):
            messages.success(self.request, "Job Application added successfully")
            return super().form_valid(form)

class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = "applications/form.html"
    success_url = reverse_lazy("application_list")
    def form_valid(self, form):
        messages.success(self.request, "Job Updated Successfully")
        return super().form_valid(form)
        

class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = JobApplication
    template_name = "applications/confirm_delete.html"
    success_url = reverse_lazy("application_list")
    def form_valid(self, form):
        messages.success(self.request, "Job application deleted successfully")
        return super().form_valid(form)
    





# def application_list(request):
#     return HttpResponse("Books section of library")