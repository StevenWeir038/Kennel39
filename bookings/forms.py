from datetime import date
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """Datefield widget in form
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pet_name', 'date', 'start_time', 'service_type']
        widgets = {
            'date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'min': date.today()
        })
