from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^template/(?P<template_id>([0-9]+))/$', views.template),
]
