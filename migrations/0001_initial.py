# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gif'
        db.create_table(u'gif_gif', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'gif', ['Gif'])


    def backwards(self, orm):
        # Deleting model 'Gif'
        db.delete_table(u'gif_gif')


    models = {
        u'gif.gif': {
            'Meta': {'object_name': 'Gif'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['gif']