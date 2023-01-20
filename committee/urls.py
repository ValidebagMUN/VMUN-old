from django.urls import path, include
from . import views

urlpatterns = [
    # Committee Home
    path('', views.home_view, name='home'),

    # Other URLS
]
