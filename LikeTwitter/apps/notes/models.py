from django.db import models
from django.contrib import admin

class Note(models.Model):
    """ Class which store notes"""
    id = models.AutoField(primary_key=True)
    body = models.TextField()
    image_of_note = models.ImageField(upload_to="note_images")
    def __unicode__(self):
        return self.body

#admin.site.register(Note)
#<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>