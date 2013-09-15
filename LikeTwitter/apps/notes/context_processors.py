from LikeTwitter.apps.notes.models import Note
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
    random_note = mark_safe(u"""<h5 id="random_note"></h5>
        <script src="js/random_note.js"></script>""")
    return {'random_note': random_note}
