from django.shortcuts import render
from django.views.generic import DetailView
from .models import Doctor

# Create your views here.
def index(request):
    doctors = Doctor.objects.all()

    return render(request, 'doctors/doctors-list.html', context= {'doctors': doctors})


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctors/doctor-detail.html'
    context_object_name = 'doctor'