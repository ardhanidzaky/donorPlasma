from django.db import models
from django.forms import ModelForm, widgets, DateInput
from .models import pendonor

class DateInput(DateInput):
    input_type = 'date'

class pendonor_form(ModelForm):
    class Meta:
        model = pendonor
        fields = ['nama','NIK','tanggal_lahir','golongan_darah','rhesus','provinsi','kota',
        'nomor_hp','bukti_swab_positif','bukti_swab_negatif','tanggal_sembuh','tanggal_terakhir_mendonor']
        widgets = {
            'tanggal_lahir' : DateInput(),
            'tanggal_sembuh' : DateInput(),
            'tanggal_terakhir_mendonor' : DateInput()
        }