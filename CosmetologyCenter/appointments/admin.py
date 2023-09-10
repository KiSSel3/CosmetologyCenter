from django.contrib import admin
from .models import AppointmentItem, Appointment


# Register your models here.
admin.site.register(AppointmentItem)

admin.site.register(Appointment)