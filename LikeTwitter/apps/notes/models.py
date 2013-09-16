from django.db import models


class Note(models.Model):
    """ Class which store notes"""
    id = models.AutoField(primary_key=True)
    body = models.TextField()
    image_of_note = models.ImageField(upload_to="note_images", blank=True,
                                      null=True)

    def __unicode__(self):
        return self.body
