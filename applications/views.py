from django.shortcuts import redirect, render
from applications.models import Application, AppList


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def view_applications(request):
    # Get all of the applications,
    applications = Application.objects.all()
    # and pass them along to the applications template.
    return render(request, 'applications.html', {'applications': applications})


def new_application(request):
    appList = AppList.objects.create()
    # Get the company of the application supplied by the form's POST request.
    Application.objects.create(
        company=request.POST['application_company'],
        app_list = appList
    )
    # Redirect to a unique URL.
    return redirect('/applications/the-only-applications-in-the-world/')
