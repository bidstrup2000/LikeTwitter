# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from LikeTwitter.apps.notes.models import Note
from django.views.generic.base import View


class AllNotesView(View):
    """
    Display List all notes of model: "LikeTwitter.apps.notes.models.Note"
    Context:
        notes:  List all notes of model: "LikeTwitter.apps.notes.models.Note"
    Template: "notes.html"
    """
    def get(self, request, **kwargs):
        """
        Response to GET request. Display lists of notes.
        """
        notes_list = Note.objects.all()
        t = loader.get_template('notes.html')
        c = Context({'notes': notes_list})
        return HttpResponse(t.render(c))


class NoteByIdView(View):
    """
    Display an individual :model:`LikeTwitter.apps.notes.models.Note`.
    **Context**
        ''Context''
        ''Notes''   An instance of :model:`LikeTwitter.apps.notes.models.Note`.
    **Template**
       template: 'search_note.html'
    """
    def get(self, request, **kwargs):
        """
        Response to GET request.
        Display 'body' of note with 'id' defined by user
        """
        if kwargs['id_of_note'] is not None:
            t = loader.get_template('search_note.html')
            c = Context({'id_of_note': kwargs['id_of_note']})
        return HttpResponse(t.render(c))
