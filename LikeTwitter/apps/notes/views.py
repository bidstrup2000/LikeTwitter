# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from LikeTwitter.apps.notes.models import Note

def index(request):
    notes_list = Note.objects.all()
    t = loader.get_template(r'notes.html')
    c = Context({'notes':notes_list})
    return HttpResponse(t.render(c))