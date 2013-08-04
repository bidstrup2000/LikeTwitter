from django.db import models
from django.contrib import admin
class Note(models.Model):
    body = models.TextField()
    def __unicode__(self):
        return self.body
        
admin.site.register(Note)
