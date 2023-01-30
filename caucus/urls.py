from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:id>/', views.caucus_view, name='caucus'),
    path('create/', views.create_view, name='create')
]