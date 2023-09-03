from django.contrib import admin
from .models import DoctorCategories, Doctor


# Register your models here.
admin.site.register(DoctorCategories)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_name', 'first_name', 'work_experience')
