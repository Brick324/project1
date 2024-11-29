from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('main_page', views.main_page),
    path('page1', views.page1),
    path('page2', views.page2),
    path('page3', views.page3)
]
