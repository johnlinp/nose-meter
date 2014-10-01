from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^elected/$', 'data_center.views.show_elected'),

    url(r'^insert/$', 'data_center.views.insert_all'),

    url(r'^tmp/$', 'data_center.views.show_tmp'),

    url(r'^$', 'data_center.views.show_all'),
    url(r'^(?P<eg_id>\d+)/$', 'data_center.views.show_all'),
    url(r'^(?P<eg_id>\d+)/(?P<ea_id>\d+)/$', 'data_center.views.show_all'),
    url(r'^(?P<eg_id>\d+)/(?P<ea_id>\d+)/(?P<pa_id>\d+)/$', 'data_center.views.show_all'),
    url(r'^(?P<eg_id>\d+)/(?P<ea_id>\d+)/(?P<pa_id>\d+)/(?P<pr_id>\d+)/$', 'data_center.views.show_promise'),
)
