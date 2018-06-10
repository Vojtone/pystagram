from django.contrib import admin
from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'gallery'

urlpatterns = [
    #/gallery/
    path('', views.index, name='index'),

    #/gallery/<username>/
    url(r'^(?P<user_username>[a-zA-Z0-9_.-]*)/$', views.detail, name="detail"),

    #/gallery/<username>/liked/
    url(r'^(?P<user_username>[a-zA-Z0-9_.-]*)/liked$', views.liked, name="liked"),
]
