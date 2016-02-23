from django.conf.urls import url

from images import views

urlpatterns = [
    url(r'^$', views.upload, name='upload'),
]
