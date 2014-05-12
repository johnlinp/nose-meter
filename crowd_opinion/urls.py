from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'crowd_opinion.views.home'),
)
