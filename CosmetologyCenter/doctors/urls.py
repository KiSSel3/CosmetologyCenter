from django.urls import path, include


app_name = 'doctors'

urlpatterns = [ 
    path('', include('django.contrib.auth.urls')),
]