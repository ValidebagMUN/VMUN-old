from django.shortcuts import render
from VMUN import settings


# Create your views here.

def home_view(request, *args, **kwargs):
    context = {
        "committee_slug": kwargs.get('committee_slug'),
        "conference_slug": kwargs.get('conference_slug'),
    }
    return render(request, "home.html", context)
