from django.urls import path, include
from .views import *

urlpatterns = [
    path('', gsl_view, name='gsl'),
]