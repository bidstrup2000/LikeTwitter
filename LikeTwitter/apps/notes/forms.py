from django import forms
from LikeTwitter.apps.notes.models import Note
from LikeTwitter.apps.notes.custom_widgets import TextareaWithAmountOfSymbol

class  Add_Form(forms.ModelForm):
    body = forms.CharField(widget = TextareaWithAmountOfSymbol, min_length=10)    
    class Meta:
        model = Note