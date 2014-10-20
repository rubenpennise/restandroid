# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoVivienda'
        db.create_table(u'web_tipovivienda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'web', ['TipoVivienda'])

        # Adding model 'Tenencia'
        db.create_table(u'web_tenencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'web', ['Tenencia'])

        # Adding model 'Vivienda'
        db.create_table(u'web_vivienda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('calle', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('tipoVivienda', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipoVivienda', to=orm['web.TipoVivienda'])),
            ('tenencia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tenencia', to=orm['web.Tenencia'])),
        ))
        db.send_create_signal(u'web', ['Vivienda'])


    def backwards(self, orm):
        # Deleting model 'TipoVivienda'
        db.delete_table(u'web_tipovivienda')

        # Deleting model 'Tenencia'
        db.delete_table(u'web_tenencia')

        # Deleting model 'Vivienda'
        db.delete_table(u'web_vivienda')


    models = {
        u'web.tenencia': {
            'Meta': {'object_name': 'Tenencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'web.tipovivienda': {
            'Meta': {'object_name': 'TipoVivienda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'web.vivienda': {
            'Meta': {'object_name': 'Vivienda'},
            'barrio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tenencia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tenencia'", 'to': u"orm['web.Tenencia']"}),
            'tipoVivienda': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipoVivienda'", 'to': u"orm['web.TipoVivienda']"})
        }
    }

    complete_apps = ['web']