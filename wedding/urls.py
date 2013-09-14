from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wedding.views.home', name='home'),
    # url(r'^wedding/', include('wedding.foo.urls')),

    url(r'^$', 'mainsite.views.base', name='base'),
    url(r'^quiz/$', 'quiz.views.quiz', name='quiz'),
    url(r'^results/$', 'quiz.views.results', name='results'),
    url(r'^wedding_party/$', 'mainsite.views.wedding_party', name='wedding_party'),
    url(r'^location/$', 'mainsite.views.location', name='location'),
    url(r'^proposal/$', 'mainsite.views.proposal', name='proposal'),
    # url(r'^login/$', 'mainsite.views.base', name='login'),
    # url(r'^newuser/$', 'mainsite.views.base', name='newuser'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
