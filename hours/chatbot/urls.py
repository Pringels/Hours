from django.conf.urls import url

from chatbot import views

urlpatterns = [
    url(r'^get_response/$', views.get_response, name='get_response'),
    url(r'^$', views.home, name='home'),
]
