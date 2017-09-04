from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^template/(?P<pk>[0-9]+)', views.template_detail),
    url(r'^templates/', views.template_list),
    url(r'^flag/(?P<pk>[0-9]+)', views.flag_detail),
    url(r'^flags/', views.flag_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)
