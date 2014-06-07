from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'crowd_opinion.views.home'),
    url(r'^district/(?P<district_name>.+)$', 'crowd_opinion.views.district'),
    url(r'^candidate/(?P<candidate_name>.+)$', 'crowd_opinion.views.candidate'),
)
