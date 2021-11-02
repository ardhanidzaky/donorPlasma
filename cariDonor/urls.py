from django.urls import path, include
from .views import *

urlpatterns = [
    path('', input_cari_donor, name='Cari Donor'),
    path('kota-by-prov', get_kota_by_prov, name='Kota By Prov'),
    path('all-prov', get_all_prov, name='All Provs'),
]
