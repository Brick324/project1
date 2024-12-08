from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('themes', views.themes, name = 'themes'),
    path('vehicles', views.vehicles, name = 'vehicles'),
    path('test', views.test, name = 'test')
]
