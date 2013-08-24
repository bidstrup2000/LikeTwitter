from django.contrib import admin
from LikeTwitter.apps.notes.models import Note
from LikeTwitter.apps.notes.forms import NewNoteForm

class NewNoteAdminForm(admin.ModelAdmin):
    """ 
    Class which will register new form with custom widget for admin interface 
    """
    form = NewNoteForm

admin.site.register(Note, NewNoteAdminForm)
