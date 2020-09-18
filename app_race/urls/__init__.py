from django.conf.urls import url, include

urlpatterns = [
    url("", include("app_race.urls.race_management")),
]
