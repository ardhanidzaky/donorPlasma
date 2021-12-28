from django.urls import path
from .views import *

urlpatterns = [
    path('', formcaridonor, name='formcaridonor'),
    path('InformasiPencariDonor', informasicaridonor, name='info'),
    path('EditData/<str:pk>/', editdata, name='EditData'),
    path('DeleteData/<str:pk>/', deletedata, name='DeleteData'),
    path('listcaridonor', listcaridonor, name='listcaridonor'),
    path('jsonnya', jsonnya, name='json'),
    path('djr', listt),
    path('djr/<pk>/', detailcaridonor),
    path('djr/update/<pk>/', update),
    path('djr/delete/<pk>/', delete),
    path('djr/create', create)
]