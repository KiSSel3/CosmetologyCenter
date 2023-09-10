from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=20, help_text='Enter first name')
    last_name = models.CharField(max_length=20, help_text='Enter last name')
    date_of_birth = models.DateField(help_text="Enter date of birth")
    email = models.EmailField(help_text="Enter email")
    town = models.CharField(help_text="Enter town", max_length=30, default='Minsk')
    phone_number = models.CharField(max_length=25, help_text='Enter phone number', validators=[RegexValidator(
        regex=r'^(\+375 \(29\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
        message='Format +375 (29) XXX-XX-XX')])

    def __str__(self):
        return f"{self.last_name} {self.first_name}"