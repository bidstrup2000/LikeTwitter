from django import forms
from LikeTwitter.apps.notes.models import Note

class  Add_Form(forms.ModelForm):
    body = forms.CharField(min_length=10)    
    class Meta:
        model = Note