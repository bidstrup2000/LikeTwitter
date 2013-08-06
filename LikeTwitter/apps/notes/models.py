from django.db import models
from django.contrib import admin
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    #primary_key = models.TextField(primary_key=True)
    body = models.TextField()
    def __unicode__(self):
        return self.body
        
admin.site.register(Note)
