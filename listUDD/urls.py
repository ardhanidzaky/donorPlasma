from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('pilihgoldar/', pilihgoldar, name='pilihgoldar'),

    path('forms/', add_forms, name='add_forms'),
    path('forms_b/', add_formsb, name='add_formsb'),
    path('forms_o/', add_formso, name='add_formso'),
    path('forms_ab/', add_formsab, name='add_formsab'),

    path('delete', delete_card, name='delete_card'),
    path('delete_b', delete_cardb, name='delete_cardb'),
    path('delete_o', delete_cardo, name='delete_cardo'),
    path('delete_ab', delete_cardab, name='delete_cardab'),

    path('edit_card', edit_card, name='edit_card'),
    path('json/', stock_json, name = 'json'),
]