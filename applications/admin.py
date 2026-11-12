from django.contrib import admin
from .models import JobApplication, Employer, Vacancy
# Register your models here.
admin.site.register(JobApplication)
admin.site.register(Vacancy)
admin.site.register(Employer)


# @admin.register(Employer)
# class EmployerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'contact_person')
#     search_fields = ('name',)
 
 
# @admin.register(Vacancy)
# class VacancyAdmin(admin.ModelAdmin):
#     list_display = ('employer', 'location',)
#     list_filter = ('employer',)
#     search_fields = ('employer',)
 
 
# @admin.register(JobApplication)
# class JobApplicationAdmin(admin.ModelAdmin):
#     list_display = ('learner_name', 'vacancy',)
#     list_filter = ('status',)
#     search_fields = ('learner_name', 'vacancy__title', 'vacancy__employer__name')
