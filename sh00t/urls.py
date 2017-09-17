from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from app import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^app/', include('app.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^logout/$', views.logout_user),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Print banner on the console when the server starts
print(settings.BANNER)

# Custom Admin Site Header
admin.site.site_header = settings.NAME

