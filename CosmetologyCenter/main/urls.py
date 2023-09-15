from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('prices/', views.price_list, name='price-list'),
    path('news/', views.news, name = 'news'),
    path('FAQ/', views.faq, name = 'FAQ'),
    path('sandbox/', views.sandbox, name = 'sandbox'),
    path('privacy_policy/', views.privacy_policy, name = 'privacy_policy'),
]