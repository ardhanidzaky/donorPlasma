from django import forms
from django.db import models
from django.forms import fields
from .models import faq

class FAQForm (forms.ModelForm):
    class Meta:
        model = faq
        fields = "__all__"

