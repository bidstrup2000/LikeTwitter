from django.shortcuts import render_to_response
from django.template import loader, Context
from django.template import RequestContext
from django.http import HttpResponse
from LikeTwitter.apps.notes.models import Note
from LikeTwitter.apps.notes.forms import NewNoteForm
from django.views.generic.base import View


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
        #Note.objects.all().delete()
        notes_list = Note.objects.all()
        form = NewNoteForm()
        return render_to_response('notes.html', {'notes': notes_list, 'form': form}, context_instance=RequestContext(request))

    def post(self, request):
        """ Adding new note with POST request. Validating input data (min 10 symbols)"""
        form = NewNoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if (len(request.FILES) == 0):
                body_of_note = form.cleaned_data['body']
                print 'without image'
                return render_to_response('note_row_ajax.html', {'note': body_of_note})
            else:
                notes_list = Note.objects.all()
                print 'with image'
                return render_to_response('notes.html', {'notes': notes_list, 'form': form}, context_instance=RequestContext(request))
        else:
            print 'Form is not valid'
            t = loader.get_template("validation_errors.html")
            c = Context({'form': form})
            return HttpResponse(t.render(c))
            #return render_to_response("validation_errors.html", {'form': form})


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
        if kwargs['id_of_note'] is not None:
            t = loader.get_template('search_note.html')
            c = Context({'id_of_note': kwargs['id_of_note']})
            return HttpResponse(t.render(c))
