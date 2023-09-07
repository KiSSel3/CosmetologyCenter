from django.urls import path, include
from . import views

app_name = 'doctors'

urlpatterns = [ 
    path('', include('django.contrib.auth.urls')),
    path('doctors/', views.index, name='doctors-list'),
    path('doctor/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
]