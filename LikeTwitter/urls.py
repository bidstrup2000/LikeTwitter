from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from LikeTwitter.apps.notes.views import NotesView

 admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^$',  NotesView.as_view(), name='notes_view'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^static/(?P<path>(css|jquery|js|images)/.+)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', NotesView.as_view(), name='notes_view'),
)
