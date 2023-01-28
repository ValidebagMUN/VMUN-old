from django.urls import path, include
from .views import home_view

urlpatterns = [
    # Conference Home
    path('', home_view, name='home'),
    # Other URLS

    # Committee URLs
    path('<slug:committee_slug>/', include('committee.urls')),
]
