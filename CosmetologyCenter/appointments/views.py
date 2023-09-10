from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentItemForm
from .models import Appointment


# Create your views here.
@login_required
def appointment_list_for_user(request):
    user = request.user
    appointments = Appointment.objects.filter(appointmentItem__service__doctor__user=user)
    return render(request, 'appointments/appointment-list.html', {'appointments': appointments})


@login_required
def create_appointment_item(request):
    if request.method == 'POST':
        form = AppointmentItemForm(request.user, request.POST)
        if form.is_valid():
            appointment_item = form.save()
            return redirect('appointments:appointment_list_for_user')
    else:
        form = AppointmentItemForm(request.user)

    return render(request, 'appointments/create-appointment-item.html', {'form': form})
