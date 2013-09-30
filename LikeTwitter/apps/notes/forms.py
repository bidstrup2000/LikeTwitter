from django import forms
from LikeTwitter.apps.notes.models import Note
from LikeTwitter.apps.notes.custom_widgets import TextareaWithAmountOfSymbol


class NewNoteForm(forms.ModelForm):
    """
    Form which contains custom widget.
    Custom Widget that extends Textarea widget and shows dynamically
    amount of symbols are writed in this field.
    """
    body = forms.CharField(initial='', widget=TextareaWithAmountOfSymbol, min_length=10)
    image_of_note = forms.ImageField(required=False)

    class Meta:
        model = Note
        fields = ['body', 'image_of_note', 'books']
