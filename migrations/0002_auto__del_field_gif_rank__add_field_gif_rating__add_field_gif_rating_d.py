# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Gif.rank'
        db.delete_column(u'gif_gif', 'rank')

        # Adding field 'Gif.rating'
        db.add_column(u'gif_gif', 'rating',
                      self.gf('django.db.models.fields.DecimalField')(default=1500, max_digits=7, decimal_places=2),
                      keep_default=False)

        # Adding field 'Gif.rating_deviation'
        db.add_column(u'gif_gif', 'rating_deviation',
                      self.gf('django.db.models.fields.DecimalField')(default=350, max_digits=7, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Gif.rank'
        db.add_column(u'gif_gif', 'rank',
                      self.gf('django.db.models.fields.IntegerField')(default=0, unique=True),
                      keep_default=False)

        # Deleting field 'Gif.rating'
        db.delete_column(u'gif_gif', 'rating')

        # Deleting field 'Gif.rating_deviation'
        db.delete_column(u'gif_gif', 'rating_deviation')


    models = {
        u'gif.gif': {
            'Meta': {'object_name': 'Gif'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '1500', 'max_digits': '7', 'decimal_places': '2'}),
            'rating_deviation': ('django.db.models.fields.DecimalField', [], {'default': '350', 'max_digits': '7', 'decimal_places': '2'})
        }
    }

    complete_apps = ['gif']