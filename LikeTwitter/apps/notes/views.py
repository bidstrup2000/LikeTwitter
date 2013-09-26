import random
from django.shortcuts import render_to_response, redirect
from django.template import loader, Context
from django.template import RequestContext
from django.http import HttpResponse
from LikeTwitter.apps.notes.models import Note
from LikeTwitter.apps.notes.forms import NewNoteForm
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse


class AllNotesView(View):
    """
    Display List all notes of model: "LikeTwitter.apps.notes.models.Note"
    Context:
        notes:  List all notes of model: "LikeTwitter.apps.notes.models.Note"
    Template: "notes.html"
    """

    def get(self, request, **kwargs):
        """
        Response to GET request. Display lists of notes. If request contains
        certain 'id' note - display 'body' of note
        """
        #Note.objects.all().delete()
        notes_list = Note.objects.all()
        return render_to_response('notes.html', {'notes': notes_list},
            context_instance=RequestContext(request))

    def post(self, request):
        if request.POST[u'id_of_note']:
            id_of_note = request.POST[u'id_of_note']
        else:
            id_of_note = None
        notes_list = Note.objects.all()
        return render_to_response('notes.html', {'notes': notes_list, 'id_of_note': id_of_note},
            context_instance=RequestContext(request))


class NoteByIdView(View):
    """
    Display selected note from model: "LikeTwitter.apps.notes.models.Note"
    Context:
        id_of_note:  id of selected note
    Template:
        "search_note.html"
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


class RandomNoteView(View):
    """Display random note from model: "LikeTwitter.apps.notes.models.Note" """

    def get(self, request):
        notes_list_len = len(Note.objects.all())
        notes_list = Note.objects.all()
        if (notes_list_len > 0):
            random_index = random.randrange(0, (notes_list_len), 1)
            random_note = notes_list[random_index]
            return HttpResponse(random_note)
        else:
            return HttpResponse("")


class AddNoteView(CreateView):
    """
    Display form for adding note("LikeTwitter.apps.notes.models.Note") to database
    Context:
        notes:  List all notes of model: "LikeTwitter.apps.notes.models.Note"
    Template: "add_note.html"
    """
    form_class = NewNoteForm
    template_name = "add_note.html"

    def get_success_url(self):
        return reverse('all_notes_view')


class AddNoteWithAjaxView(CreateView):
    """
    Display form for adding note("LikeTwitter.apps.notes.models.Note") to database
    Template: "add_note_with_ajax.html"
    """

    form_class = NewNoteForm
    template_name = "add_note_with_ajax.html"

    def get_success_url(self):
        return reverse('all_notes_view')

    def post(self, request):
        """
        Adding new note with POST request. Validating input data
        (min 10 symbols)
        """
        form = NewNoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if (len(request.FILES) == 0):
                return HttpResponse(self.get_success_url())
            else:
                return redirect(self.get_success_url())
        else:
            t = loader.get_template("validation_errors.html")
            c = Context({'form': form})
            return HttpResponse(t.render(c))
