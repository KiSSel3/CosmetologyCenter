from django.db import models
from django.contrib.auth.models import User
from services.models import Service
from main.models import Client


# Create your models here.
class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    appointmentItem = models.ForeignKey('AppointmentItem', on_delete=models.CASCADE)


class AppointmentItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    time = models.TimeField(default=None)

    class Meta:
        ordering = ["date", "time"]

    def __str__(self):
        return f"{self.date} {self.time}"