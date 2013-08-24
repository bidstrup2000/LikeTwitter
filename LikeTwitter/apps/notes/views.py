from django.shortcuts import render_to_response 
from django.template import loader, Context
from django.template import RequestContext
from django.http import HttpResponse
from LikeTwitter.apps.notes.models import Note
from LikeTwitter.apps.notes.forms import NewNoteForm
from django.views.generic.base import View
from django.utils import simplejson

class AllNotesView(View):        
    """
    Display an individual :model:`LikeTwitter.apps.notes.models.Note`.
    **Context**
    ''Context''
    ''Notes'' An instance of :model:`LikeTwitter.apps.notes.models.Note`.
    **Template:**
        :template: 'notes.html'
    """
    def get(self, request, **kwargs):
        """
        Response to GET request. Display lists of notes. If request contains certain 'id' note - 
        display 'body' of note         
        """
        notes_list = Note.objects.all()
        form = NewNoteForm()
        return render_to_response('notes.html', {'notes':notes_list, 'form': form}, context_instance=RequestContext(request)) 
    def post(self,request):
        """ Adding new note with POST request. Validating input data (min 10 symbols)"""
        form = NewNoteForm(request.POST)
        if form.is_valid():
            form.save()
            body_of_note = form.cleaned_data['body']
            t = loader.get_template('note_row_ajax.html')
            c = Context({'note':body_of_note})
            #json = simplejson.dumps({'body_of_note':body_of_note})            
            #return HttpResponse(json, mimetype='application/json')
            return render_to_response('note_row_ajax.html', {'note':body_of_note})
        else:
            return False

class NoteByIdView(View):
    """
    Display an individual :model:`LikeTwitter.apps.notes.models.Note`.
    **Context**
    ''Context''
    ''Notes'' An instance of :model:`LikeTwitter.apps.notes.models.Note`.
    **Template**
    template: 'search_note.html'
    """
    def get(self, request, **kwargs):
        """
        Response to GET request.
        Display 'body' of note with 'id' defined by user
        """        
        if kwargs['id_of_note'] != None:
            t = loader.get_template('search_note.html')
            c = Context({'id_of_note':kwargs['id_of_note']})
            return HttpResponse(t.render(c))




