from django.db import models
from django.contrib import admin


class Book(models.Model):
    """Class which store "LikeTwitter.apps.notes.models.Note" """
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Note(models.Model):
    """ Class which contain user note"""
    body = models.TextField()
    image_of_note = models.ImageField(upload_to="note_images", blank=True,
                                      null=True)
    books = models.ManyToManyField(Book, blank=True, null=True)

    def __unicode__(self):
        return self.body

admin.site.register(Book)
