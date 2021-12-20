from django.urls import path, include
from .views import *

urlpatterns = [
    path('', input_cari_donor, name='Cari Donor'),
    path('kota-by-prov', get_kota_by_prov, name='Kota By Prov'),
    path('all-prov', get_all_prov, name='All Prov'),
    path('all-kota', get_all_kota, name='All Kota'),
    path('json-pendonor', get_pendonor_http, name='JSON Pendonor'),
]
