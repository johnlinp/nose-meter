from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'data_center.views.home'),
)
