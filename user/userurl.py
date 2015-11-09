__author__ = 'mityagov_vi'

from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^$', views.user_list),
    url(r'^(?P<pk>[\w]+)$', views.user_detail),
]
