from django.db import models
from django.urls import reverse
from doctors.models import Doctor


class Service(models.Model):
    service_name = models.CharField(max_length=30, help_text="Enter service name")
    service_type = models.ForeignKey('ServiceType', on_delete=models.SET_NULL, null=True, help_text="Choose service type")

    office = models.OneToOneField('Office', on_delete=models.CASCADE, help_text="Choose an office")
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, help_text="Choose a doctor")

    image = models.ImageField(upload_to='images', blank=True, null=True)


    def __str__(self):
        return self.service_name


    # def get_absolute_url(self):
    #     return reverse('service-detail-view', args=[str(self.id)])


class ServiceType(models.Model):
    designation = models.CharField(max_length=25, help_text="Enter type")


    def __str__(self):
        return self.designation


class Office(models.Model):
    number = models.IntegerField()


    def __str__(self):
        return str(self.number)    