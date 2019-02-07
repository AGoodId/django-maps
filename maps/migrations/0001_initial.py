# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GMap'
        db.create_table(u'maps_gmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('formatted_address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('geocode_error', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('geocode_error_message', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'maps', ['GMap'])


    def backwards(self, orm):
        # Deleting model 'GMap'
        db.delete_table(u'maps_gmap')


    models = {
        u'maps.gmap': {
            'Meta': {'object_name': 'GMap'},
            'address': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'formatted_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'geocode_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'geocode_error_message': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['maps']