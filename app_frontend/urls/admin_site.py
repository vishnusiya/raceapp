from django.conf.urls import url
from django.conf.urls import url
from app_frontend.views import admin_site

urlpatterns = [
  url(r'^$', admin_site.login_user),
  url(r'^login/$', admin_site.login_user),
  url(r'^logout/$', admin_site.logout_user),
  url(r'^query/search/$', admin_site.query_search),
]