from django.urls import path
from .views import *

urlpatterns = [
    path('', formcaridonor, name='formcaridonor'),
    path('InformasiPencariDonor', informasicaridonor, name='info'),
    path('EditData/<str:pk>/', editdata, name='EditData'),
    path('DeleteData/<str:pk>/', deletedata, name='DeleteData'),
    path('listcaridonor', listcaridonor, name='listcaridonor'),
    path('jsonnya', jsonnya, name='json')
]