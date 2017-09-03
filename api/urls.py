from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'flags', views.FlagViewSet)

urlpatterns = [
    url(r'^template/(?P<template_id>([0-9]+))/$', views.template),
    url(r'^', include(router.urls)),
]

