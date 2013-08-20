from LikeTwitter.apps.notes.models import Note
def count_of_notes(request):
    count_of_notes = Note.objects.count()
    return {'total_count_of_notes': count_of_notes}