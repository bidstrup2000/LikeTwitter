from LikeTwitter.apps.notes.models import Note
"""
Custom context processor which add few custom variables 
to template
"""

def count_of_notes(request):
    """ Return total count of notes"""
    count_of_notes = Note.objects.count()
    return {'total_count_of_notes': count_of_notes}