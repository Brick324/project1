from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('vehicles', views.vehicles, name = 'vehicles'),
    path('car', views.car, name = 'car'),
    path('carbody', views.carbody, name = 'carbody'),
    path('electrical', views.electrical, name = 'electrical'),
    path('engine', views.engine, name = 'engine'),
    path('transmission', views.transmission, name = 'transmission'),
    path('plane', views.plane, name = 'plane'),
    path('fuselage', views.fuselage, name = 'fuselage'),
    path('landinggear', views.landinggear, name = 'landinggear'),
    path('tail', views.tail, name = 'tail'),
    path('turbine', views.turbine, name = 'turbine'),
    path('wing', views.wing, name = 'wing'),
    path('train', views.train, name = 'train'),
    path('trainbody', views.trainbody, name = 'trainbody'),
    path('roof', views.roof, name = 'roof'),
    path('electrobox', views.electrobox, name = 'electrobox'),
    path('register', views.register, name = 'register'),
    path('login', views.register, name = 'login'),
    path('start', views.start_quiz_view, name='start'),
    path('get-questions/start', views.get_questions, {'is_start': True}, name='get-questions'),
    path('get-questions', views.get_questions, {'is_start': False}, name='get-questions'),
    path('get-answer', views.get_answer, name='get-answer'),
    path('get-finish', views.get_finish, name='get-finish'),
]