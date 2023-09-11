from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.appointment_list_for_user, name='appointment_list_for_user'),
    path('create_appointment_item/', views.create_appointment_item, name='create_appointment_item'),
    path('create_appointments/', views.create_appointments, name='create_appointments'),
]