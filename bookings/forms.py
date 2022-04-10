from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pet_name', 'date', 'start_time', 'service_type']
        # Apply date picker direct to a rendered modelForm https://code-examples.net/en/q/f993c1
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker'})
            }
