# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Circu(models.Model):
    dpto = models.IntegerField()
    circu1 = models.CharField(max_length=5)
    circ = models.IntegerField()
    descir = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'circu'

class Escuela(models.Model):
    codigo = models.IntegerField()
    desest = models.CharField(max_length=40)
    direst = models.CharField(max_length=40)
    circ = models.IntegerField()
    circu = models.CharField(max_length=5)
    descir = models.CharField(max_length=25)
    secc = models.IntegerField()
    dessec = models.CharField(max_length=20)
    cp = models.CharField(max_length=8)
    mesas = models.IntegerField()
    md = models.IntegerField()
    mh = models.IntegerField()
    cantf = models.IntegerField()
    cexe = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'escuela'

class Patoca(models.Model):
    dni = models.IntegerField()
    clase = models.CharField(max_length=4)
    apenom = models.CharField(max_length=80)
    profes = models.CharField(max_length=7)
    domic = models.CharField(max_length=34)
    analf = models.CharField(max_length=1)
    tipdoc = models.CharField(max_length=7)
    secc = models.IntegerField()
    circu = models.IntegerField()
    mesa = models.IntegerField()
    sexo = models.CharField(max_length=1)
    adf = models.CharField(max_length=1)
    orden = models.BigIntegerField()
    cod_pp = models.IntegerField()
    afi = models.IntegerField()
    partido = models.CharField(max_length=13)
    class Meta:
        managed = False
        db_table = 'patoca'

class Seccion(models.Model):
    dpto = models.IntegerField()
    dessec = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'seccion'

