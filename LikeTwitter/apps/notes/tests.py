from django.core.urlresolvers import reverse
from django_webtest import WebTest
from LikeTwitter.apps.notes.models import Note


class My_test_case(WebTest):
    """
    Class which inherits from WebTest and do tests of notes application
    """
    fixtures = [r'fixtures\notes.json']

    def test_ticket1_create_app_that_shows_list_of_text_notes(self):
        """ Check web page for presence all note records from db"""
        note_list = Note.objects.all()
        page = self.app.get(reverse('notes_view'))
        for note_string in note_list:
            assert note_string in page
