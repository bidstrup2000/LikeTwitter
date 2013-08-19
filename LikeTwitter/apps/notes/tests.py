from django.core.urlresolvers import reverse
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
        page = self.app.get(reverse('index')).form
        text_of_notes = {'Integer quis ipsum tincidunt, rutrum augue non, molestie dui.',
                         'Nam id feugiat velit, quis placerat nisl. Nulla vel sagittis justo.',
                         'Duis facilisis nisl id tempor ultricies.',
                         'Duis at dolor neque',}
        for t in text_of_notes:
            page['body'] = t
            self.assertEqual(page['id_symbol_count'].value, len(t))
            #page.submit()

    def test_ticket4_write_custom_widget_admin_interface(self):
            page = self.app.get(reverse('admin')).form
            page['id_username'] = 'Andrii'
            page['id_password'] = 'Pamukkale2009'
            page = page.submit().follow()
            page = self.app.get(reverse('/admin/notes/note/add/')).form
            text_of_notes = {'Integer quis ipsum tincidunt, rutrum augue non, molestie dui.',
                             'Nam id feugiat velit, quis placerat nisl. Nulla vel sagittis justo.',
                             'Duis facilisis nisl id tempor ultricies.',
                             'Duis at dolor neque',}
            for t in text_of_notes:
                page['body'] = t
                self.assertEqual(page['id_symbol_count'].value, len(t))
       