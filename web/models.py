from django.db import models

class TipoVivienda(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Tenencia(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Vivienda(models.Model):
	barrio = models.CharField(max_length=100)
	calle = models.CharField(max_length=100)
	numero = models.CharField(max_length=20)
	tipoVivienda = models.ForeignKey(TipoVivienda,related_name='tipoVivienda')
	tenencia = models.ForeignKey(Tenencia,related_name="tenencia")

	def __unicode__(self):
		return self.calle



# Create your models here.
