from django import forms
from LikeTwitter.apps.notes.models import Note
from django.contrib import admin
from LikeTwitter.apps.notes.custom_widgets import TextareaWithAmountOfSymbol

class  NewNoteForm(forms.ModelForm):
    body = forms.CharField(widget = TextareaWithAmountOfSymbol, min_length=10)    
    class Meta:
        model = Note

