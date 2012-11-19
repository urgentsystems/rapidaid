# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Unit'
        db.create_table('urgentapp_unit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('urgentapp', ['Unit'])


    def backwards(self, orm):
        # Deleting model 'Unit'
        db.delete_table('urgentapp_unit')


    models = {
        'urgentapp.unit': {
            'Meta': {'object_name': 'Unit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unit_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['urgentapp']