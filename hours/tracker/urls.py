from django.conf.urls import url

from tracker import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_hours$', views.get_hours, name='get_hours'),
    url(r'^redeem_hour$', views.redeem_hour, name='redeem_hour'),
    url(r'^spend_hours$', views.spend_hours, name='spend_hours'),
    url(r'^spend_game_hour$', views.spend_game_hour, name='spend_game_hour'),
]
