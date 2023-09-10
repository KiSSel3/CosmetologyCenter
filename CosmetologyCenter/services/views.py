from django.shortcuts import render
from django.views.generic import DetailView
from .models import Service
from cart.form import AppointmentItemForm 


# Create your views here.
def index(request):
    services = Service.objects.all()

    return render(request, 'services/services-list.html', context= {'services':services})


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service-detail.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.object
        context['form'] = AppointmentItemForm(service=service)
        return context