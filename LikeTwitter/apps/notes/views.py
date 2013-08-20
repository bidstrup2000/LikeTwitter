from django.shortcuts import render_to_response 

# Create your views here.
from django.template import loader, Context
from django.template import RequestContext
from django.http import HttpResponse
from LikeTwitter.apps.notes.models import Note
from LikeTwitter.apps.notes.forms import NewNoteForm

def index(request):
    #m = Note.objects.filter(pk__gt=7).delete()
    notes_list = Note.objects.all()
    t = loader.get_template(r'notes.html')
    c = Context({'notes':notes_list})
    if request.method == "POST":
        #request with data
        form = NewNoteForm(request.POST)
        if form.is_valid(): 
            form.save()
    else:
         form = NewNoteForm()
    return render_to_response('notes.html', {'notes':notes_list, 'form': form}, context_instance=RequestContext(request)) 
def search_id(request, id_of_note):
    t = loader.get_template(r'search_note.html')
    c = Context({'id_of_note':id_of_note})
    return HttpResponse(t.render(c))



