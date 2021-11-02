from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('tryLogin', tryLogin, name='tryLogin'),
    path('register', register_request, name='register'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('daftar', daftar, name='daftar'),
]