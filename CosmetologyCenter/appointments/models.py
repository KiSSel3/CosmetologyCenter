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
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.datetime.hour}:{self.datetime.minute}  {self.datetime.day}.{self.datetime.month}"