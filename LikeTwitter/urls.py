from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from LikeTwitter.apps.notes.views import NotesView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',  NotesView.as_view(), name='NotesView'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^static/(?P<path>(css|jquery|js|images)/.+)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),     
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', NotesView.as_view(), name='NotesView'),
)
#r'(?:.*?/)?
#urlpatterns += staticfiles_urlpatterns()
#if settings.DEBUG:
#    urlpatterns += patterns('django.contrib.staticfiles.views',
#        url(r'^static/(?P<path>.*)$', 'serve'),
#    )
