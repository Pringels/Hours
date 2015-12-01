from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^(?P<slug>[A-Za-z0-9_\-.]+)?/?$', views.post, name='post'),
]
