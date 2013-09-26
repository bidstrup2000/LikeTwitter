from LikeTwitter.apps.notes.models import Note
from django import template
#from django.core.context_processors import static

register = template.Library()


@register.inclusion_tag('search_note_by_id.html')
def search_note(id_of_note):
    """ Return note by id from page template tag """
    try:
        note = Note.objects.get(id=int(id_of_note))
    except:
        note = 'Note not found'
    return {'searched_note': note}
