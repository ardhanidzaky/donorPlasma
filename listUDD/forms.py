from django import forms
from .models import Stok, StokB, StokAB, StokO

class StokForm(forms.ModelForm):
	class Meta:
		model = Stok
		fields = "__all__"

class StokBForm(forms.ModelForm):
	class Meta:
		model = StokB
		fields = "__all__"

class StokOForm(forms.ModelForm):
	class Meta:
		model = StokO
		fields = "__all__"

class StokABForm(forms.ModelForm):
	class Meta:
		model = StokAB
		fields = "__all__"