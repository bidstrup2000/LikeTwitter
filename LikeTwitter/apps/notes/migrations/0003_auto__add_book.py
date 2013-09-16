# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'notes_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'notes', ['Book'])

        # Adding M2M table for field books on 'Note'
        m2m_table_name = db.shorten_name(u'notes_note_books')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('note', models.ForeignKey(orm[u'notes.note'], null=False)),
            ('book', models.ForeignKey(orm[u'notes.book'], null=False))
        ))
        db.create_unique(m2m_table_name, ['note_id', 'book_id'])

    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'notes_book')

        # Removing M2M table for field books on 'Note'
        db.delete_table(db.shorten_name(u'notes_note_books'))

    models = {
        u'notes.book': {
            'Meta': {'object_name': 'Book'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'notes.note': {
            'Meta': {'object_name': 'Note'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['notes.Book']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_of_note': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['notes']
