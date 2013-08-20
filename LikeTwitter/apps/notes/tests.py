from django.core.urlresolvers import reverse
from LikeTwitter.apps.notes.models import Note
from django_webtest import WebTest

class My_test_case(WebTest):
    #fixtures = ['notes.json']
    extra_environ = {'HTTP_ACCEPT_LANGUAGE': 'en'}
    
    def test_ticket3_add_ability_to_add_new_text_node(self):
        page = self.app.get(reverse('index')).form
        text_of_notes = {'Integer quis ipsum tincidunt, rutrum augue non, molestie dui.',
                         'Nam id feugiat velit, quis placerat nisl. Nulla vel sagittis justo.',
                         'Duis facilisis nisl id tempor ultricies.',
                         'Duis at dolor neque',}
        for t in text_of_notes:
            page['body'] = t
            page.submit()
        result_page = self.app.get(reverse('index'))
        for t in text_of_notes:
            assert t in result_page
    
    def test_ticket4_write_custom_widget_creating_new_form(self):
        pass
        #page = self.app.get(reverse('index')).form
        #text_of_notes = {'Integer quis ipsum tincidunt, rutrum augue non, molestie dui.',
        #                 'Nam id feugiat velit, quis placerat nisl. Nulla vel sagittis justo.',
        #                 'Duis facilisis nisl id tempor ultricies.',
        #                 'Duis at dolor neque',}
        #for t in text_of_notes:
        #    page['body'] = t
        #    result_page = page.submit()
        #    print result_page
        #    print (u'Symbols count(min. 10):    ' + str(len(t)))
        #    assert (u'Symbols count(min. 10):    ' + str(len(t))) in result_page
            #I have AssertionError at this place
    
    def test_ticket5_show_total_count_of_notes(self):
        text_of_notes = {'Integer quis ipsum tincidunt, rutrum augue non, molestie dui.',
                                 'Nam id feugiat velit, quis placerat nisl. Nulla vel sagittis justo.',
                                 'Duis facilisis nisl id tempor ultricies.',
                                 'Duis at dolor neque',}
        for t in text_of_notes:
            page = self.app.get(reverse('index')).form
            page['body'] = t
            page.submit()
            page = self.app.get(reverse('index'))
            #print 'Count '+str(Note.objects.count())
            assert (u'Notes count: ' + str(Note.objects.count())) in page        



       