from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^template/(?P<pk>[0-9]+)', views.template_detail),
    url(r'^templates/', views.template_list),
    url(r'^flag/(?P<pk>[0-9]+)', views.flag_detail),
    url(r'^flags/', views.flag_list),
    url(r'^sh0t/(?P<pk>[0-9]+)', views.sh0t_detail),
    url(r'^sh0ts/', views.sh0t_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)