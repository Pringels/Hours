from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('blog.urls')),
    url(r'^tracker/', include('tracker.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
