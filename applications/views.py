from django.shortcuts import redirect, render
from applications.models import Application


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Application.objects.create(
            company=request.POST['application_company']
        )
        return redirect('/')

    return render(request, 'home.html')
