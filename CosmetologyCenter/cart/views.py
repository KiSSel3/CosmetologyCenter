from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart
from services.models import Service
from cart.form import AppointmentItemForm
from appointments.models import AppointmentItem
from django.core.exceptions import PermissionDenied
from appointments.models import AppointmentItem


def add_to_cart(request, service_id):
    if request.method == 'POST':
        service = get_object_or_404(Service, id=service_id)
        form = AppointmentItemForm(request.POST, service = service)

        if form.is_valid():
            cart = Cart(request)
            cart.add(form.cleaned_data['appointment_item'])
        else:
            print(form.errors)
    return redirect('services:services-list')


def cart_details(request):
    cart = Cart(request)
    return render(request, 'cart/cart-detail.html', {'cart': cart})
  

def cart_remove(request, appointment_item_id):
  if not request.user.is_authenticated:
      raise PermissionDenied("No acsess")

  cart = Cart(request)
  appointment_item = get_object_or_404(AppointmentItem, id=appointment_item_id)
  cart.remove(appointment_item)
  return redirect('cart:cart_details')


