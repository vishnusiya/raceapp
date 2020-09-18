from django.conf.urls import url
# from django.urls import path

from app_race.views import race_management


urlpatterns = [
    url(r'^user/login/$', race_management.user_login),
    url(r'^create/player/details$', race_management.api_create_player_details),
    url(r'^player/list/get$', race_management.api_player_list_get),
    ]