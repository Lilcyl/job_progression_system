from django.contrib import admin
from .models import JobApplication, Employer, Vacancy
# Register your models here.
admin.site.register(JobApplication)
admin.site.register(Vacancy)
admin.site.register(Employer)