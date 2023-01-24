from django.urls import path, include
from . import views


urlpatterns = [
    path('mod/<int:id>/', views.mod_view, name='mod'),
    path('unmod/<int:id>/', views.unmod_view, name='unmod'),
    path('semimod/<int:id>/', views.semimod_view, name='semimod'),
    path('create/', views.create_view, name='create')
]