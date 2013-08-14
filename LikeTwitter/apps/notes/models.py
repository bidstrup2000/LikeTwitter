from django.db import models
from django.contrib import admin
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.TextField()
    def __unicode__(self):
        return self.body
    #def __init__(self, text_of_note):
    #    self.body =  text_of_note
        
admin.site.register(Note)
