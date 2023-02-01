"""VMUN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
import conference
from .views import *


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', home_view, name='home'),
    path('', include('authentication.urls')),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),

    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('sentry-debug/', trigger_error),
    path("__reload__/", include("django_browser_reload.urls")),
    path('__debug__/', include('debug_toolbar.urls')),

    # Conference urls
    path('<slug:conference_slug>/', include('conference.urls')),
]
