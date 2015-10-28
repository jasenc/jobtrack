from django.shortcuts import redirect, render
from applications.models import Application, AppList


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def view_applications(request, app_list_id):
    appList = AppList.objects.get(id=app_list_id)
    return render(request, 'applications.html', {'appList': appList})


def new_application(request):
    appList = AppList.objects.create()
    # Get the company of the application supplied by the form's POST request.
    Application.objects.create(
        company=request.POST['application_company'],
        app_list=appList
    )
    # Redirect to a unique URL.
    return redirect('/applications/{0}/'.format(appList.id))


def add_application(request, app_list_id):
    appList = AppList.objects.get(id=app_list_id)
    Application.objects.create(company=request.POST['application_company'],
                               app_list=appList)
    return redirect('/applications/{0}/'.format(appList.id))
