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
    path('create_rewiew/', views.create_review, name = 'create_rewiew'),
    path('rewiews/', views.reviews, name = 'rewiews'),
    path('privacy_policy/', views.privacy_policy, name = 'privacy_policy'),
    path("promotional_code/", views.promotional_code, name='promotional_code'),
    path('vacancies/', views.vacancies, name = 'vacancies'),
    path('js_sandbox/', views.js_sandbox, name = 'js_sandbox')
]