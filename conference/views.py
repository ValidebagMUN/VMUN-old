from django.http import HttpResponse
from django.shortcuts import render
from VMUN import settings

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {
        "conference_slug": kwargs.get('conference_slug'),
    }
    return render(request, "home.html", context)