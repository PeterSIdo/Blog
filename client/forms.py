from django import forms
from .models import Client, TreatmentSession
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'condition', 'treatment']
class TreatmentSessionForm(forms.ModelForm):
    class Meta:
        model = TreatmentSession
        fields = ['date_time', 'treatment_notes']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }