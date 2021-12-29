from django.urls import path
from .views import *

urlpatterns = [
    path('',informasi_pendonor,name='informasi_pendonor'),
    path('daftar',form_pendonor,name='daftar_donor'),
    path('json',data_pendonor,name='json'),
    path('delete',delete_pendonor,name='delete_pendonor'),
    path('update',update_pendonor,name='update_pendonor'),
    path('get_user',get_pendonor, name='get_pendonor'),
    path('get_info', info_donor, name='info_donor'),
    path('add_pendonor', daftar_donor, name='daftar_donor')
]