from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add-article', add_article, name='add-article'),
    path('<str:uniq>/', detail_article, name='detail-article'),
    path('load-more', load_more, name='load-more'),
]
