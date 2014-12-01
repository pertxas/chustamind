from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'djangoChustaMind.views.home', name='home'),
    url(r'^game$', 'djangoChustaMind.views.game', name='game'),
    url(r'^newgame$', 'djangoChustaMind.views.newgame', name='newgame'),
    url(r'^undo', 'djangoChustaMind.views.undo', name='undo'),
    url(r'^tst', 'djangoChustaMind.views.tst', name='tst'),
    url(r'^usrinput/(?P<n>[0-9]+)$', 'djangoChustaMind.views.usrinput', name='usrinput'),
    url(r'^btn/(?P<n>[0-9]+)$', 'djangoChustaMind.views.btn', name='btn'),
    url(r'^peg/(?P<n>[0-9]+)$', 'djangoChustaMind.views.peg', name='peg'),
    # url(r'^djangoChustaMind/', include('djangoChustaMind.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
