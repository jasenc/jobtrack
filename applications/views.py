from django.shortcuts import render
from applications.models import Application


# Create your views here.
def home_page(request):
    application = Application()
    application.company = request.POST.get('application_company', '')
    application.save()

    return render(request, 'home.html', {
        'new_application_company': application.company
    })
