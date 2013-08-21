from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
#from LikeTwitter import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'LikeTwitter.apps.notes.views.index', name='index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'(?:.*?/)?(?P<path>(css|jquery|js|images)/.+)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),     
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', 'LikeTwitter.apps.notes.views.index', name='index'),
)
