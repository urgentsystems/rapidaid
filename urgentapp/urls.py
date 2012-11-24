from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from urgentapp import views

urlpatterns = patterns('',
    url(r'^units/$', views.UnitList.as_view()),
    url(r'^units/(?P<pk>[0-9]+)/$', views.UnitDetail.as_view()),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserInstance.as_view())
)