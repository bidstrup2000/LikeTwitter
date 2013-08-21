from django.core.urlresolvers import reverse 
from django_webtest import WebTest
from LikeTwitter.apps.notes.models import Note

class My_test_case(WebTest):    
    #fixtures = ['fixtures\notes.json']
    
    def test_ticket1_create_app_that_shows_list_of_text_notes(self):
        note_list = Note.objects.all()
        page = self.app.get(reverse('index'))
        for note_string in note_list:
            assert note_string in page