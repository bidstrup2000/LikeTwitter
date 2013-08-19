from django import forms
from string import Template
from django.utils.safestring import mark_safe

class TextareaWithAmountOfSymbol(forms.Textarea):
   def render(self, name, value, attrs=None):
      tpl = Template(u"""
      <textarea cols="40" id="id_body" name="body" rows="10">$body</textarea>
      <h5 id="id_symbol_count" name = "symbols_count"></h5>
      <script src="js/text_area_with_counter.js"></script>                
      """)
      return mark_safe(tpl.substitute(body = value))
# <script type="text/javascript" src="{{ STATIC_URL }}js/jquery-1.10.2.min.js"></script>
# <script src="http://code.jquery.com/jquery-latest.js"></script>
# <script type="text/javascript" language="javascript" src="{% static 'js/jquery-1.10.2.min.js'%}"></script>   
#return mark_safe(tpl.substitute(body = value))
#jQuery("#id_body").after();
