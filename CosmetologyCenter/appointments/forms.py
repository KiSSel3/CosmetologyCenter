from django import forms
from .models import AppointmentItem
from services.models import Service
from main.models import Client


class AppointmentItemForm(forms.ModelForm):
    class Meta:
        model = AppointmentItem
        fields = ['service', 'date', 'time']

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(doctor__user=user)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'town', 'phone_number']