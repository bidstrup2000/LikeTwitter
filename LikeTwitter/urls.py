from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from LikeTwitter import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'LikeTwitter.apps.notes.views.index', name='index'),
    # url(r'^LikeTwitter/', include('LikeTwitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^notes/', include('LikeTwitter.apps.notes.views')),    
    #url(r'^notes/(?P<id_of_note>[0-9]+)', 'LikeTwitter.apps.notes.templates', name='search_id'),
    
    #
    url(r'(?:.*?/)?(?P<path>(css|jquery|jscripts|images)/.+)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }), 
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    url(r'^add/$', 'LikeTwitter.apps.notes.views.add_note', name='add_note'),        
    url(r'^notes/(?P<id_of_note>[0-9]+)', 'LikeTwitter.apps.notes.views.search_id', name='search_id'),    
    url(r'^notes/$', 'LikeTwitter.apps.notes.views.index', name='index'),
)
#urlpatterns += patterns('', (
#    r'^static/(?P<path>.*)$',
#    'django.views.static.serve',
#    {'document_root': settings.STATIC_ROOT}
#))
