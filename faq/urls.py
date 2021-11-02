from django.urls import path
from .views import delete_question, index, json, add_forms

urlpatterns = [
    path('', index, name='index'),
    path('formfaq/', add_forms, name='add_forms'),
    path('delete', delete_question, name='delete_question'),
    path('json/', json, name = 'json'),
]