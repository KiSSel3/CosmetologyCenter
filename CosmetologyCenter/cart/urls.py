from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_details, name='cart_details'),
    path('add_to_cart/<int:service_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_in_cart/<int:appointment_item_id>/', views.cart_remove, name='cart_remove'),
]