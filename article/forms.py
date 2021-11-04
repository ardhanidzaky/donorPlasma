from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = ['foto', 'judul', 'isi']
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'isi': forms.Textarea(attrs={'class': 'form-control'})
        }
