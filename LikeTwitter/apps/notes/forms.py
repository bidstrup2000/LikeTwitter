from django import forms
from LikeTwitter.apps.notes.models import Note


class Add_Form(forms.ModelForm):
    """ Class which validate data from user form"""
    body = forms.CharField(min_length=10)

    class Meta:
        model = Note
