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
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
