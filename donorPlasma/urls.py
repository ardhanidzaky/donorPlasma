"""donorPlasma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from home.views import home as homePage
from formCariDonor.views import *
from listUDD.views import *
from faq.views import *
from cariDonor.views import *
from pendonor.views import *
from article.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('FormCariDonor/', include('formCariDonor.urls')),
    path('informasiUDD/', include('listUDD.urls')),
    path('faq/', include('faq.urls')),
    path('pendonor/', include('pendonor.urls')),
    path('cari-donor/', include('cariDonor.urls')),
    path('article/', include('article.urls')),
    re_path(r'^$', homePage, name='homePage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
