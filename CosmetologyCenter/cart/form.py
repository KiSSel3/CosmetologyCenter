from django import forms
from appointments.models import AppointmentItem


class AppointmentItemForm(forms.Form):
    appointment_item = forms.ModelChoiceField(
        queryset=AppointmentItem.objects.none(),
        label="Выберите удобное для вас время"
    )

    def __init__(self, *args, **kwargs):
        service = kwargs.pop('service')
        super().__init__(*args, **kwargs)
        self.fields['appointment_item'].queryset = AppointmentItem.objects.filter(service=service)
        