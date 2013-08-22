# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from LikeTwitter.apps.notes.models import Note
from django.views.generic.base import View

class NotesView(View):
    """
        Display an individual :model:`LikeTwitter.apps.notes.models.Note`.
    **Context**
    ''Context''
    ''Notes''
         An instance of :model:`LikeTwitter.apps.notes.models.Note`.
    **Template:**
         :template: 'notes.html'
    """
    
    def get(self, request):
        """ Response to GET request. Display lists of notes."""
        notes_list = Note.objects.all()
        t = loader.get_template('notes.html')
        c = Context({'notes':notes_list})
        return HttpResponse(t.render(c))