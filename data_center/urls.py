from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^tmp$', 'data_center.views.show_tmp'),

    url(r'^$', 'data_center.views.show_all'),
    url(r'^(?P<eg_id>\d+)/$', 'data_center.views.show_all'),
    url(r'^(?P<eg_id>\d+)/(?P<ea_id>\d+)/$', 'data_center.views.show_all'),
    url(r'^(?P<eg_id>\d+)/(?P<ea_id>\d+)/(?P<p_id>\d+)/$', 'data_center.views.show_all'),
)
