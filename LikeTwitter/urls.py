from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from LikeTwitter.apps.notes.views import AllNotesView, NoteByIdView 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',  AllNotesView.as_view(), name='AllNotesView'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'(?:.*?/)?(?P<path>(css|jquery|js|images)/.+)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }), 
    url(r'^notes/(?P<id_of_note>[0-9]+)', NoteByIdView.as_view() , name='NoteByIdView'),   
    url(r'^notes/', AllNotesView.as_view(), name='AllNotesView'),
)

