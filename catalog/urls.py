from django.urls import path
from . import views
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/$', views.NewsListView.as_view(), name='news'),
    url(r'^news/(?P<pk>\d+)$', views.NewsDetailView.as_view(), name='news-detail'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/', tag_detail, name='tag_detail_url')
]
