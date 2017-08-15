from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('app.urls'))
]