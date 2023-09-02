from django.contrib import admin
from .models import DoctorCategories, Doctor


# Register your models here.
admin.site.register(DoctorCategories)
admin.site.register(Doctor)