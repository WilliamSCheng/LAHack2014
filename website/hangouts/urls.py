from django.conf.urls import patterns, include, url
from website.hangouts.views import HangoutListView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inner_project.views.home', name='home'),
    # url(r'^inner_project/', include('inner_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^hangout_list/$', HangoutListView.as_view(), name='hangout_list'),

)
