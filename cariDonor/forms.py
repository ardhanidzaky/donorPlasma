from django import forms
from .models import Donor

class cariDonor(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
