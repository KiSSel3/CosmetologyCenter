from django.shortcuts import render
from .models import Service 


# Create your views here.
def index(request):
    services = Service.objects.all()

    return render(request, 'services/services-list.html', context= {'services':services})