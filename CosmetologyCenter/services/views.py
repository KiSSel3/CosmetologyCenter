from django.shortcuts import render
from django.views.generic import DetailView
from .models import Service 


# Create your views here.
def index(request):
    services = Service.objects.all()

    return render(request, 'services/services-list.html', context= {'services':services})


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service-detail.html'
    context_object_name = 'service'