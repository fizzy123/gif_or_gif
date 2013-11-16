# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Gif.last_updated'
        db.add_column(u'gif_gif', 'last_updated',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2000, 1, 1, 0, 0), auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Gif.last_updated'
        db.delete_column(u'gif_gif', 'last_updated')


    models = {
        u'gif.gif': {
            'Meta': {'object_name': 'Gif'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '1500', 'max_digits': '7', 'decimal_places': '2'}),
            'rating_deviation': ('django.db.models.fields.DecimalField', [], {'default': '350', 'max_digits': '7', 'decimal_places': '2'})
        }
    }

    complete_apps = ['gif']