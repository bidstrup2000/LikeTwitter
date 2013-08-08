# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from LikeTwitter.apps.notes.models import Note
from LikeTwitter.apps.notes.forms import Add_Form

def index(request):
    notes_list = Note.objects.all()
    t = loader.get_template(r'notes.html')
    c = Context({'notes':notes_list})
    #return HttpResponse(t.render(c))
    if request.method == "POST":
        form = Add_Form(request.POST)
        if form.is_valid():
            #return HttpResponseRedirect("/note/")
            form.save()
        #render_to_response('notes.html', {'notes':notes_list, 'form': form}) 
    else:
        form = Add_Form()
    return render_to_response('notes.html', {'notes':notes_list, 'form': form}) 
def search_id(request, id_of_note):
    t = loader.get_template(r'search_note.html')
    c = Context({'id_of_note':id_of_note})
    return HttpResponse(t.render(c))

def add_note(request):
    

