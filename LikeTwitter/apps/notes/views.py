# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from LikeTwitter.apps.notes.models import Note

def index(request):
    notes_list = Note.objects.all()
    t = loader.get_template(r'notes.html')
    c = Context({'notes':notes_list})
    return HttpResponse(t.render(c))

def search_id(request, id_of_note):
    t = loader.get_template(r'search_note.html')
    c = Context({'id_of_note':id_of_note})
    return HttpResponse(t.render(c))

