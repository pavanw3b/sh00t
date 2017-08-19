from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from app import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^app/flags', views.flag, name='flag'),
    url(r'^admin/', admin.site.urls),
    url(r'^', views.index, name='index'),
    url(r'^tinymce/', include('tinymce.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
