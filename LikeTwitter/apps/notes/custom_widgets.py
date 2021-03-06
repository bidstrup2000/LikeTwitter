from django import forms
from string import Template
from django.utils.safestring import mark_safe


class TextareaWithAmountOfSymbol(forms.Textarea):
    """
    Custom form widget which show amount of entered symbols_count
    """

    def render(self, name, value, attrs=None):
        """ Render custom widget with amount of symbols"""
        tpl = Template(u"""
            <textarea cols="40" id="id_body" name="body" rows="10">$body</textarea>
            <h5 id="id_symbol_count" name = "symbols_count"></h5>
            <script type="text/javascript" language="javascript" src="js/jquery-1.10.2.min.js"></script>
            <script src="js/text_area_with_counter.js"></script>
            """)
        return mark_safe(tpl.substitute(body=value))
