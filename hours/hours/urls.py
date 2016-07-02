from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', include('images.urls')),
    url(r'^rsvp/', include('gedeck.urls')),
    url(r'^bonsai/', include('bonsai.urls', namespace="bonsai")),
    url(r'^', include('blog.urls', namespace="blog")),
]
