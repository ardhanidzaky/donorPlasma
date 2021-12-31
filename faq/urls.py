from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('formfaq/', add_forms, name='add_forms'),
    path('delete', delete_question, name='delete_question'),
    path('json/', json_faq, name = 'json'),
    path('add_faq/', add_faq, name = 'add_faq'),
]