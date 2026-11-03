
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