from . import views
from django.urls import path

app_name = 'stats'

urlpatterns = [
    path('report/', views.report, name='report'),
]