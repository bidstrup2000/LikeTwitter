from django.contrib import admin
from LikeTwitter.apps.notes.models import Note
from LikeTwitter.apps.notes.forms import NewNoteForm

class NewNoteAdminForm(admin.ModelAdmin):
    form = NewNoteForm

admin.site.register(Note, NewNoteAdminForm)
