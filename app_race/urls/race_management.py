from django.conf.urls import url
# from django.urls import path

from app_race.views import race_management


urlpatterns = [
    url(r'^user/login/$', race_management.user_login),
    url(r'^create/result/details$', race_management.api_create_result_details),
    url(r'^result/list/get$', race_management.api_result_list_get),
    ]