from LikeTwitter.apps.notes.models import Note
from django import template
from django.template.loader import get_template

register = template.Library()
t = get_template('search_by_id.html')

def search_by_id(id_of_note):
    note = Note.objects.get(pk=id_of_note)
    return {'searched_note': note}

register.inclusion_tag(t)(search_by_id)