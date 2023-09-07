from django.shortcuts import render
from services.models import Service, ServiceType

# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def price_list(request):
    service_types = ServiceType.objects.all()
    services_by_type = {}
    
    for service_type in service_types:
        services = Service.objects.filter(service_type=service_type)
        services_by_type[service_type] = services

    return render(request, 'main/price-list.html', {'services_by_type': services_by_type, 'service_types': service_types})