from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('crowd_opinion.urls')),
    url(r'^data/', include('data_center.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
