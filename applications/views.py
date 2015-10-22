from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return render(request, 'home.html', {
        'new_application_text': request.POST.get('application_text', ''),
    })
