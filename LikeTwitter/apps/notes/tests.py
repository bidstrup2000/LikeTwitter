from django.core.urlresolvers import reverse
from django_webtest import WebTest
from LikeTwitter.apps.notes.models import Note


class My_test_case(WebTest):
    """
    Class which inherits from WebTest and do tests of notes application
    """
    fixtures = [r'fixtures\notes.json']

    def test_ticket1_create_app_that_shows_list_of_text_notes(self):
        """ Check web page for presence all note records from database"""
        note_list = Note.objects.all()
        page = self.app.get(reverse('all_notes_view'))
        for note_string in note_list:
            assert note_string in page

    def test_ticket2_create_custom_inclusion_template_tag(self):
        """ Check web page for presence searched note"""
        note_list = Note.objects.all()
        for note in note_list:
            #Pass id of note in GET request and try to find 'body' of note in response page
            page = self.app.get(reverse('note_by_id_view'), kwargs={'id_of_note': note.id})
            assert note.body in page

    def test_ticket3_add_ability_to_add_new_text_node(self):
        """ Check updated page for new note entered via form. """
        page = self.app.get(reverse('all_notes_view')).form
        text_of_notes = {
            'Integer quis ipsum tincidunt, rutrum augue non, molestie dui',
            'Nam id feugiat velit, quis placerat nisl. Nulla vel sagittis justo.',
            'Duis facilisis nisl id tempor ultricies.',
            'Duis at dolor neque'}
        for t in text_of_notes:
            page['body'] = t
            page.submit()
        result_page = self.app.get(reverse('all_notes_view'))
        for t in text_of_notes:
            assert t in result_page
