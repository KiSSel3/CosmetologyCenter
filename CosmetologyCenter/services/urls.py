from django.urls import path, include
from . import views

app_name = 'services'

urlpatterns = [ 
    path('', views.index, name='services-list'),
]