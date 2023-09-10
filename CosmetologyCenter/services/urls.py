from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [ 
    path('', views.index, name='services-list'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
]