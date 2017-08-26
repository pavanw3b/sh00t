from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from app import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^app/flags/$', views.flags),
    url(r'^app/flag/([0-9]+)/$', views.flag),
    url(r'^app/sh0ts/$', views.sh0ts),
    url(r'^app/sh0t/([0-9]+)/$', views.sh0t),
    url(r'^app/assessments/$', views.assessments),
    url(r'^app/assessment/([0-9]+)/$', views.assessment),
    url(r'^app/projects/$', views.projects),
    url(r'^app/project/([0-9]+)/$', views.project),
    url(r'^app/templates/$', views.templates),
    url(r'^app/template/([0-9]+)/$', views.template),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^logout/$', views.logout_user),
    url(r'^$', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Print banner on the console when the server starts
print(settings.BANNER)

# Custom Admin Site Header
admin.site.site_header = settings.NAME

