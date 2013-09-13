from django import forms
from LikeTwitter.apps.notes.models import Note
from LikeTwitter.apps.notes.custom_widgets import TextareaWithAmountOfSymbol


class NewNoteForm(forms.ModelForm):
    """
<<<<<<< HEAD
    Form which contains custom widget.
=======
    Form which contains custom widget.l
>>>>>>> t7_add_ability_to_attach_an_image_to_note
    Custom Widget that extends Textarea widget and shows dynamically
    amount of symbols are writed in this field.
    """
    body = forms.CharField(widget=TextareaWithAmountOfSymbol, min_length=10)

    class Meta:
        model = Note
        fields = ['body', 'image_of_note']
