from django.conf.urls import url

from . import views

app_name = 'testapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mac_id>[0-9]+)/$', views.detail, name='detail')
]