from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), # Committee Home

    path('caucus/', include('caucus.urls')), # Caucus URLs
    path('resolution/', include('resolution.urls')), # Resolution URLs
    path('gsl/', include('gsl.urls')), # GSL URLs

    # Roll Call URL
    # TODO: Add Roll Call View
]
