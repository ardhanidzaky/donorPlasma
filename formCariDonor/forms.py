from django.forms import ModelForm
from .models import CariDonor
from django import forms
from django.forms.widgets import DateInput

class DateInput(forms.DateInput):
    input_type = 'date'

class CariDonorForm(ModelForm):
    class Meta:
        model = CariDonor
        fields = '__all__'
        widgets = {
            'tanggal_Lahir': DateInput()
        }