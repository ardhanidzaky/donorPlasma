from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add-article', add_article, name='add-article'),
    path('<str:uniq>/', detail_article, name='detail-article'),
    path('load-more', load_more, name='load-more'),
    path('get-artikel', get_artikel, name='get-artikel'),
    path('post-artikel', post_artikel, name='post-artikel')
]
