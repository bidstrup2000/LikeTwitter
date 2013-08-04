from django.db import models
from django.contrib import admin
class note(models.Model):
    body = models.TextField()
admin.site.register(note)
