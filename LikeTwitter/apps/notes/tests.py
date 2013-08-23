from django.core.urlresolvers import reverse 
from django_webtest import WebTest
from LikeTwitter.apps.notes.models import Note

class My_test_case(WebTest): 
    """
    Class which inherits from WebTest and do tests of notes application
    """
    fixtures = ['fixtures\notes.json']
    def test_ticket1_create_app_that_shows_list_of_text_notes(self):
        """ Check web page for presence all note records from db""" 
        note_list = Note.objects.all()
        page = self.app.get(reverse('AllNotesView'))
        for note_string in note_list:
            assert note_string in page
            
    def test_ticket2_create_custom_inclusion_template_tag(self):
        """ Check web page for presence searched note""" 
        note_list = Note.objects.all()
        for note in note_list:
            #Pass id of note in GET request and try to find 'body' of note in response page
            page = self.app.get(reverse('NoteByIdView'), kwargs={'id_of_note': note.id})
            assert note.body in page
    
    