from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from LikeTwitter.apps.notes.views import AllNotesView, NoteByIdView, RandomNoteView, AddNoteView, AddNoteWithAjaxView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$',  AllNotesView.as_view(), name='all_notes_view'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'(?:.*?/)?(?P<path>(css|js)/.+)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^add_note/$', AddNoteView.as_view(), name="add_note"),
    url(r'^add_note_with_ajax/$', AddNoteWithAjaxView.as_view(), name="add_note_with_ajax"),
    url(r'^notes/(?P<id_of_note>[0-9]+)', NoteByIdView.as_view(), name='note_by_id_view'),
    url(r'^notes/$', AllNotesView.as_view(), name='all_notes_view'),
    url(r'^random/$', RandomNoteView.as_view(), name='random_note_view')
)
if settings.DEBUG:
    urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT}))
