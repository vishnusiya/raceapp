from django.conf.urls import url, include

urlpatterns = [
    url('', include('app_frontend.urls.admin_site')),
]