from django.db import models
from django.urls import reverse


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=20, help_text='Enter first name')
    last_name = models.CharField(max_length=20, help_text='Enter last name')
    date_of_birth = models.DateField(help_text="Enter date of birth")
    email = models.EmailField(help_text="Enter email")
    town = models.CharField(help_text="Enter town", max_length=30, default='Minsk')
    phone_number = models.CharField(max_length=15, help_text='Enter phone number')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])