from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'crowd_opinion.views.home'),
    url(r'^district/(?P<county_name>.+)$', 'crowd_opinion.views.district'),
)
