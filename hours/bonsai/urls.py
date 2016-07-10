from django.conf.urls import url

from bonsai import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^$', views.home, name='home'),
    url(r'^update/$', views.update, name='update'),
    url(r'^fetch/$', views.fetch, name='fetch'),
    url(r'^fetch_more/$', views.fetch_more, name='fetch_more'),
]
