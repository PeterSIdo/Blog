from django import forms
from .models import Client, TreatmentSession

class DateInput(forms.DateInput):
    input_type = 'date'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'dob', 'condition', 'treatment']
        widgets = {
            'dob': DateInput()
        }

class TreatmentSessionForm(forms.ModelForm):
    class Meta:
        model = TreatmentSession
        fields = ['date_time', 'treatment_notes']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
