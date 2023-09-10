from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.appointment_list_for_user, name='appointment_list_for_user'),
    path('create/', views.create_appointment_item, name='create_appointment_item'),
]