# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Departamento'
        db.create_table(u'web_departamento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'web', ['Departamento'])

        # Adding model 'Municipio'
        db.create_table(u'web_municipio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Departamento'])),
        ))
        db.send_create_signal(u'web', ['Municipio'])

        # Adding model 'Localidad'
        db.create_table(u'web_localidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Municipio'])),
        ))
        db.send_create_signal(u'web', ['Localidad'])

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

        # Adding model 'Servicio'
        db.create_table(u'web_servicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agua', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('luz', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gas', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'web', ['Servicio'])

        # Adding model 'Banio'
        db.create_table(u'web_banio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('si', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('no', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'web', ['Banio'])

        # Adding model 'Vivienda'
        db.create_table(u'web_vivienda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('calle', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('piso', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('dpto', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('tipoVivienda', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipoVivienda', to=orm['web.TipoVivienda'])),
            ('tenencia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tenencia', to=orm['web.Tenencia'])),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='servicio', to=orm['web.Servicio'])),
            ('banio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='banio', to=orm['web.Banio'])),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='departamento', to=orm['web.Departamento'])),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='municipio', to=orm['web.Municipio'])),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='localidad', to=orm['web.Localidad'])),
        ))
        db.send_create_signal(u'web', ['Vivienda'])

        # Adding model 'CoberturaSalud'
        db.create_table(u'web_coberturasalud', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'web', ['CoberturaSalud'])

        # Adding model 'Discapacidad'
        db.create_table(u'web_discapacidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'web', ['Discapacidad'])

        # Adding model 'NivelAprobado'
        db.create_table(u'web_nivelaprobado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'web', ['NivelAprobado'])

        # Adding model 'MotivosAbandono'
        db.create_table(u'web_motivosabandono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'web', ['MotivosAbandono'])

        # Adding model 'Oficio'
        db.create_table(u'web_oficio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'web', ['Oficio'])

        # Adding model 'CondicionActividad'
        db.create_table(u'web_condicionactividad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'web', ['CondicionActividad'])

        # Adding model 'Persona'
        db.create_table(u'web_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apeNombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('fechaNac', self.gf('django.db.models.fields.DateField')()),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('correo', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('vivienda', self.gf('django.db.models.fields.related.ForeignKey')(related_name='vivienda', to=orm['web.Vivienda'])),
            ('cobertura', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cobertura', to=orm['web.CoberturaSalud'])),
            ('discapacidad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='discapacidad', to=orm['web.Discapacidad'])),
            ('nivelAprobado', self.gf('django.db.models.fields.related.ForeignKey')(related_name='nivelAprobado', to=orm['web.NivelAprobado'])),
            ('motivosAbanono', self.gf('django.db.models.fields.related.ForeignKey')(related_name='motivosAbandono', to=orm['web.MotivosAbandono'])),
            ('oficio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='oficio', to=orm['web.Oficio'])),
            ('condicionActividad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='condicionActividad', to=orm['web.CondicionActividad'])),
        ))
        db.send_create_signal(u'web', ['Persona'])


    def backwards(self, orm):
        # Deleting model 'Departamento'
        db.delete_table(u'web_departamento')

        # Deleting model 'Municipio'
        db.delete_table(u'web_municipio')

        # Deleting model 'Localidad'
        db.delete_table(u'web_localidad')

        # Deleting model 'TipoVivienda'
        db.delete_table(u'web_tipovivienda')

        # Deleting model 'Tenencia'
        db.delete_table(u'web_tenencia')

        # Deleting model 'Servicio'
        db.delete_table(u'web_servicio')

        # Deleting model 'Banio'
        db.delete_table(u'web_banio')

        # Deleting model 'Vivienda'
        db.delete_table(u'web_vivienda')

        # Deleting model 'CoberturaSalud'
        db.delete_table(u'web_coberturasalud')

        # Deleting model 'Discapacidad'
        db.delete_table(u'web_discapacidad')

        # Deleting model 'NivelAprobado'
        db.delete_table(u'web_nivelaprobado')

        # Deleting model 'MotivosAbandono'
        db.delete_table(u'web_motivosabandono')

        # Deleting model 'Oficio'
        db.delete_table(u'web_oficio')

        # Deleting model 'CondicionActividad'
        db.delete_table(u'web_condicionactividad')

        # Deleting model 'Persona'
        db.delete_table(u'web_persona')


    models = {
        u'web.banio': {
            'Meta': {'object_name': 'Banio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'si': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'web.coberturasalud': {
            'Meta': {'object_name': 'CoberturaSalud'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'web.condicionactividad': {
            'Meta': {'object_name': 'CondicionActividad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'web.departamento': {
            'Meta': {'object_name': 'Departamento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'web.discapacidad': {
            'Meta': {'object_name': 'Discapacidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'web.localidad': {
            'Meta': {'object_name': 'Localidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'web.motivosabandono': {
            'Meta': {'object_name': 'MotivosAbandono'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'web.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Departamento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'web.nivelaprobado': {
            'Meta': {'object_name': 'NivelAprobado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'web.oficio': {
            'Meta': {'object_name': 'Oficio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'web.persona': {
            'Meta': {'object_name': 'Persona'},
            'apeNombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cobertura': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cobertura'", 'to': u"orm['web.CoberturaSalud']"}),
            'condicionActividad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'condicionActividad'", 'to': u"orm['web.CondicionActividad']"}),
            'correo': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'discapacidad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'discapacidad'", 'to': u"orm['web.Discapacidad']"}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fechaNac': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivosAbanono': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'motivosAbandono'", 'to': u"orm['web.MotivosAbandono']"}),
            'nivelAprobado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'nivelAprobado'", 'to': u"orm['web.NivelAprobado']"}),
            'oficio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'oficio'", 'to': u"orm['web.Oficio']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vivienda': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vivienda'", 'to': u"orm['web.Vivienda']"})
        },
        u'web.servicio': {
            'Meta': {'object_name': 'Servicio'},
            'agua': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'luz': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
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
            'banio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'banio'", 'to': u"orm['web.Banio']"}),
            'barrio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'departamento'", 'to': u"orm['web.Departamento']"}),
            'dpto': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'localidad'", 'to': u"orm['web.Localidad']"}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'municipio'", 'to': u"orm['web.Municipio']"}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'piso': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'servicio'", 'to': u"orm['web.Servicio']"}),
            'tenencia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tenencia'", 'to': u"orm['web.Tenencia']"}),
            'tipoVivienda': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipoVivienda'", 'to': u"orm['web.TipoVivienda']"})
        }
    }

    complete_apps = ['web']