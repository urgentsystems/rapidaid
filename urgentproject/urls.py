from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'urgentapp.views.index'),
    url(r'^units.kml', 'urgentapp.views.get_units'),
    # url(r'^urgentproject/', include('urgentproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),


    url(r'^api/', include('urgentapp.urls')),


    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))


)


urlpatterns += staticfiles_urlpatterns()