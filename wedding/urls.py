from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mainsite.views.base', name='base'),
    url(r'^quiz/$', 'quiz.views.quiz', name='quiz'),
    url(r'^results/$', 'quiz.views.results', name='results'),
    url(r'^wedding_party/$', 'mainsite.views.wedding_party',
        name='wedding_party'),
    url(r'^location/$', 'mainsite.views.location', name='location'),
    url(r'^story/$', 'mainsite.views.story', name='story'),
    url(r'^high_scores/$', 'quiz.views.high_scores', name='high_scores'),
    url(r'^photos/$', 'photoalbum.views.photo_album', name='photo_album'),
    url(r'^guestbook/$', 'mainsite.views.guestbook', name='guestbook'),
    url(r'^map/$', 'mainsite.views.map', name='map'),
    url(r'^afterparty/$', 'mainsite.views.afterparty', name='afterparty'),
    url(r'^lodging/$', 'mainsite.views.lodging', name='lodging'),
    url(r'^social/', include('socialregistration.urls',
        namespace='socialregistration')),
    # url(r'^login/$', 'mainsite.views.base', name='login'),
    # url(r'^newuser/$', 'mainsite.views.base', name='newuser'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


import settings
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )