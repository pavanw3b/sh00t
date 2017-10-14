from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^flag/(?P<pk>[0-9]+)', views.flag_detail),
    url(r'^flags/', views.flag_list),
    url(r'^sh0t/(?P<pk>[0-9]+)', views.sh0t_detail),
    url(r'^sh0ts/', views.sh0t_list),
    url(r'^assessment/(?P<pk>[0-9]+)', views.assessment_detail),
    url(r'^assessments/', views.assessment_list),
    url(r'^project/(?P<pk>[0-9]+)', views.project_detail),
    url(r'^projects/', views.project_detail),
    url(r'^template/(?P<pk>[0-9]+)', views.template_detail),
    url(r'^templates/', views.template_list),
    url(r'^case-master/(?P<pk>[0-9]+)', views.case_master_detail),
    url(r'^case-masters/', views.case_master_list),
    url(r'^module-master/(?P<pk>[0-9]+)', views.module_master_detail),
    url(r'^module-masters/', views.module_master_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)
