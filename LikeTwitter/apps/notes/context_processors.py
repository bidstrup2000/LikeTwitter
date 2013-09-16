from LikeTwitter.apps.notes.models import Note
from LikeTwitter import settings
from django.utils.safestring import mark_safe
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
    random_note = mark_safe(u"""<div id="random_note" class="col-md-4"></div><script type="text/javascript"
        language="javascript" src=""" + static_url + """js/random_note.js></script>""")
    return {'random_note': random_note}
