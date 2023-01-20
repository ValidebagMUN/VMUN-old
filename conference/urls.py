from django.urls import path, include
from . import views

urlpatterns = [
    # Conference Home
    path('', views.home_view, name='home'),
    # Other URLS

    # Committee URLs
    path('<slug:committee_slug>/', include('committee.urls')),
]
