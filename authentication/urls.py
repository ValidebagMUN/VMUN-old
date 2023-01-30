from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView
from .views import home_view

urlpatterns = [
    path('', home_view, name = 'home'),
    path('login/', LoginView.as_view(template_name = 'login.html') , name = 'login'),
]