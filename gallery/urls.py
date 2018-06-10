from django.contrib import admin
from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'gallery'

urlpatterns = [
    #/gallery/
    path('', views.index, name='index'),

    #/gallery/<username>/
    url(r'^(?P<user_username>[a-zA-Z0-9_.-]*)/$', views.grid, name="grid"),

    #/gallery/<username>/liked/
    url(r'^(?P<user_username>[a-zA-Z0-9_.-]*)/liked/$', views.liked, name="liked"),

    #dopisuje
    #/gallery/<username>/<photo_id>/
    url(r'^(?P<user_username>[a-zA-Z0-9_.-]*)/(?P<photo_id>[0-9]+)/$', views.detail, name="detail"),
]
