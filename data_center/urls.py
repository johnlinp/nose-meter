from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'data_center.views.show_all'),
    url(r'^(?P<eg_id>\d+)/$', 'data_center.views.show_all'),
)
