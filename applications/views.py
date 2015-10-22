from django.shortcuts import redirect, render
from applications.models import Application


# Create your views here.
def home_page(request):
    # If the request is POST,
    if request.method == 'POST':
        # create a new application object
        Application.objects.create(
            # while setting the company of the application equal to the value
            # supplier by the POST form.
            company=request.POST['application_company']
        )
        # Then redirect back to the home page.
        return redirect('/')

    # Get all of the applications,
    applications = Application.objects.all()
    # Otherwise render a GET request of the home page and pass all of the
    # applications along.
    return render(request, 'home.html', {'applications': applications})
