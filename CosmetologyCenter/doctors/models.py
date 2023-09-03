from django.contrib.auth.models import User
from django.db import models


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    first_name = models.CharField(max_length=20, help_text="Enter type")
    last_name = models.CharField(max_length=20, help_text="Enter type")

    category = models.ManyToManyField('DoctorCategories', help_text="Choose doctor category")

    work_experience = models.IntegerField(help_text="Enter work experience")


    class Meta:
        ordering = ["last_name", "first_name"]


    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class DoctorCategories(models.Model):
    designation = models.CharField(max_length=20, help_text="Enter type")

    def __str__(self):
        return self.designation