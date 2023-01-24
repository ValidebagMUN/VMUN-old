from django.shortcuts import render
from conference import models

# Create your views here.


def home_view(request):
    context = {
        'conferences': models.Conference.objects.all(),
    }
    return render(request, 'site_index.html', context)


def login_view(request):
    return render(request, 'login.html', {})