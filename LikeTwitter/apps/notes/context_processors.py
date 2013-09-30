from LikeTwitter.apps.notes.models import Note
from LikeTwitter import settings
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

"""
Custom context processor which add few custom variables
to template
"""


def count_of_notes(request):
    """ Return total count of notes"""
    count_of_notes = Note.objects.count()
    return {'total_count_of_notes': count_of_notes}


def random_note(request):
    static_url = settings.STATIC_URL
    site = "http://" + str(Site.objects.get_current().domain)
    random_note_full_url = mark_safe(u"""<div id="random_note" class="col-md-4"></div><script type="text/javascript"
        language="javascript" src="%s%sjs/random_note.js"></script>""" % (site, static_url))
    random_note_local_url = mark_safe(u"""<div id="random_note" class="col-md-4"></div><script type="text/javascript"
        language="javascript" src="%sjs/random_note.js"></script>""" % (static_url))
    return {'random_note_full_url': random_note_full_url, 'random_note_local_url': random_note_local_url}


def site_url(request):
    """ Return current site url"""
    site = "http://" + str(Site.objects.get_current().domain)
    return {'site_url': site}
