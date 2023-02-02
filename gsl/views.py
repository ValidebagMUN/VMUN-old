from django.shortcuts import render

# Create your views here.

def gsl_view(request, *args, **kwargs):
    context = {
        'conference_slug': kwargs['conference_slug'],
        'committee_slug': kwargs['committee_slug'],
    }
    return render(request, 'gsl.html', context)