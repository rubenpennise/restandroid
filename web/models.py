# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
from padron.models import *
import hashlib 
class Departamento(models.Model):
	nombre = models.CharField(max_length=75)

	def __unicode__(self):
		return self.nombre

class Municipio(models.Model):
	nombre = models.CharField(max_length=75)
	departamento = models.ForeignKey(Departamento)

	def __unicode__(self):
		return self.nombre

class Localidad(models.Model):
	nombre = models.CharField(max_length=75)
	municipio = models.ForeignKey(Municipio)

	def __unicode__(self):
		return self.nombre


class TipoVivienda(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Tenencia(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Servicio(models.Model):
	agua = models.BooleanField(default=False)
	luz = models.BooleanField(default=False)
	gas = models.BooleanField(default=False)
	telefono = models.BooleanField(default=False)
	cloacas = models.BooleanField(default=False)
	def __unicode__(self):
		respuesta = ""
		if self.agua:
			respuesta += "Agua: Si "
		if self.luz:
			respuesta += "Luz: Si "
		if self.gas:
			respuesta += "Gas: Si "
		if self.telefono:
			respuesta += "Teléfono: Si "
		if self.cloacas:
			respuesta += "Cloacas: Si "
		return respuesta

class Banio(models.Model):
	si = models.BooleanField(default=False)
	no = models.BooleanField(default=False)

	def __unicode__(self):
		if self.si:
			return "Si"
		else:
			return "No"

class Vivienda(models.Model):
	barrio = models.CharField(max_length=1000)
	calle = models.CharField(max_length=1000)
	numero = models.CharField(max_length=20)
	piso = models.CharField(max_length=20,blank=True)
	dpto = models.CharField(max_length=10,blank=True)
	tipoVivienda = models.ForeignKey(TipoVivienda,related_name='tipoVivienda', verbose_name="Tipo de vivienda")
	tenencia = models.ForeignKey(Tenencia,related_name="tenencia")
	servicio = models.ForeignKey(Servicio,related_name="servicio")
	banio = models.ForeignKey(Banio,related_name="banio", verbose_name="Baño")
	departamento = models.ForeignKey(Departamento,related_name="departamento")
	municipio = models.ForeignKey(Municipio,related_name="municipio")
	localidad = models.ForeignKey(Localidad,related_name="localidad")

	cantidadHabitaciones = models.IntegerField("Cantidad de habitaciones",null=True,blank=True)
	urgenciasBasicas = models.CharField("Urgencias básicas", max_length=20000,null=True, blank=True)


	def __unicode__(self):
		return self.calle

class CoberturaSalud(models.Model):
	nombre = models.CharField(max_length=75)
	
	def __unicode__(self):
		return self.nombre


class Discapacidad(models.Model):
	nombre = models.CharField(max_length=75)
	
	def __unicode__(self):
		return self.nombre


class NivelAprobado(models.Model):
	nombre = models.CharField(max_length=75)
	
	def __unicode__(self):
		return self.nombre


class MotivosAbandono(models.Model):
	nombre = models.CharField(max_length=75)
	
	def __unicode__(self):
		return self.nombre


class Oficio(models.Model):
	nombre = models.CharField(max_length=75)

	def __unicode__(self):
		return self.nombre

class CondicionActividad(models.Model):
	nombre = models.CharField(max_length=75)

	def __unicode__(self):
		return self.nombre


class EstadoSalud(models.Model):
	nombre = models.CharField(max_length="300")
	descripcion = models.CharField(max_length="2000")

class SaludReproductiva(models.Model):
	OPCIONES_EMBARAZO_RIESGOSO = (
        ('SI', 'SI'),
        ('NO', 'NO'),
        ('NS - NC', 'NO SABE - NO CONTESTA'),
        )
	OPCIONES_TIPO_DE_ANTICONCEPTIVO = (
        ('PASTILLAS', 'PASTILLAS'),
        ('OVULOS', 'OVULOS'),
        ('PRESERVATIVO', 'PRESERVATIVO'),
        ('ESPIRAL - DIU', 'ESPIRAL - DIU'),
        ('DIAFRAGMA', 'DIAFRAGMA'),
        ('RITMO - CONTROL PERIODO MENSTRUAL', 'RITMO - CONTROL PERIODO MENSTRUAL'),
        ('OTRO METODO', 'OTRO METODO'),
        ('NS - NC', 'NO SABE - NO CONTESTA'),

        )
	OPCIONES_LUGARES_DE_CONTROL = (
		('PUBLICO', 'ESTABLECIMIENTO PUBLICO'),
		('PRIVADO', 'ESTABLECIMIENTO PRIVADO'),
		('OTRO', 'OTRO LUGAR'),
		('NS - NC', 'NO SABE - NO CONTESTA'),
			)
	OPCIONES_TIPO_DE_PARTO = (
		('NORMAL', 'NORMAL'),
		('CESAREA', 'CESAREA'),
		('NS - NC', 'NO SABE - NO CONTESTA'),
			)
	OPCIONES_TIPO_DE_ABORTO = (
		('OBSTETRICO', 'OBSTETRICO'),
		('PROVOCADO', 'PROVOCADO'),
		('ESPONTANEO', 'ESPONTANEO'),
		('NS - NC', 'NO SABE - NO CONTESTA'),
			)
	OPCIONES_LUGAR_DE_OCURRENCIA = (
		('PUBLICO', 'ESTABLE PUBLICO'),
		('PRIVADO', 'ESTABLE PRIVADO'),
		('PARTICULAR', 'DOMICILIO PARTICULAR'),
		('OTRO', 'OTRO LUGAR'),
		('NS - NC', 'NO SABE - NO CONTESTA'),
			)
	

	usoDeAnticonceptivo = models.BooleanField(default=False)
	tipoDeAnticonceptivo = models.CharField(max_length=100,choices=OPCIONES_TIPO_DE_ANTICONCEPTIVO)
	fechaUltimaMenstruacion = models.DateField(default=datetime.now)
	fechaProbableParto =  models.DateField(default=datetime.now)
	embarazoRiesgoso = models.CharField(max_length=100,choices=OPCIONES_EMBARAZO_RIESGOSO)
	lugaresDeControl = models.CharField(max_length=100,choices=OPCIONES_LUGARES_DE_CONTROL)
	tipoDeParto = models.CharField(max_length=100,choices=OPCIONES_TIPO_DE_PARTO)
	tipoDeAborto = models.CharField(max_length=100,choices=OPCIONES_TIPO_DE_ABORTO)
	lugarDeAborto = models.CharField(max_length=100,choices=OPCIONES_LUGAR_DE_OCURRENCIA)

class Persona(models.Model):
	apeNombre = models.CharField("Nombre y apellido", max_length=100)
	dni = models.CharField(max_length=30)
	fechaNac = models.DateField(default=datetime.now)
	sexo = models.CharField(max_length=10)
	telefono = models.CharField(max_length=20,null=True, blank=True)
	correo = models.CharField(max_length=75,null=True, blank=True)
	vivienda = models.ForeignKey(Vivienda,related_name="vivienda",null=True, blank=True)
	cobertura = models.ForeignKey(CoberturaSalud,related_name="cobertura",null=True, blank=True, verbose_name="Cobertura de salud")
	discapacidad = models.ForeignKey(Discapacidad,related_name="discapacidad",null=True, blank=True)
	nivelAprobado = models.ForeignKey(NivelAprobado,related_name="nivelAprobado",null=True, blank=True,verbose_name="Nivel aprobado")
	motivosAbandono = models.ForeignKey(MotivosAbandono,related_name="motivosAbandono",null=True, blank=True,verbose_name="Motivos de abandono")
	oficio = models.ForeignKey(Oficio,related_name="oficio",null=True, blank=True)
	condicionActividad = models.ForeignKey(CondicionActividad,related_name="condicionActividad",null=True, blank=True,verbose_name=u"Condición de actividad")
	domicilioPadron = models.CharField(max_length=300, null=True, blank=True)
	analfPadron = models.CharField(max_length=3, null=True, blank=True)
	seccPadron = models.IntegerField("Sección", null=True, blank=True)
	circuPadron = models.IntegerField("Circuito", null=True, blank=True)
	mesaPadron = models.IntegerField("Mesa", null=True, blank=True)
	partidoPadron = models.CharField("Partido", max_length=100, null=True, blank=True)

	jefeDeHogar = models.BooleanField(default=False)
	estadoSalud = models.ForeignKey(EstadoSalud, related_name="estadoSalud",null=True, blank=True,verbose_name=u"estado de salud")
	infoAdicional = models.CharField("Información  adicional", blank=True, null=True, max_length=2000)
	


	saludReproductiva = models.ForeignKey(SaludReproductiva, related_name="saludReproductiva", null=True, blank=True)

	def save(self, *args, **kwargs):
		try:
			persona_padron = Patoca.objects.using('padron').get(dni=self.dni)
			self.domicilioPadron = persona_padron.domic
			self.analfPadron = persona_padron.analf    
			self.seccPadron = persona_padron.secc
			self.circuPadron = persona_padron.circu
			self.mesaPadron = persona_padron.mesa
			self.partidoPadron = persona_padron.partido
			super(Persona, self).save(*args, **kwargs)
		except	Patoca.DoesNotExist:
			super(Persona, self).save(*args, **kwargs)

class Encuesta(models.Model):
	pregunta = models.CharField(max_length=350)
	respuestaSi = models.IntegerField()
	respuestaNo = models.IntegerField()
	respuestaNoSabe = models.IntegerField()
	fecha = models.DateField()
	codigo = models.IntegerField(blank=True)


class Pregunta(models.Model):
	pregunta = models.CharField(max_length=400)
	fecha = models.DateField()
	codigo = models.IntegerField(blank=True,null=True)

class Respuesta(models.Model):
	respuesta = models.CharField(max_length=400)
	resultado = models.IntegerField()
	codigo = models.IntegerField(blank=True,null=True)
	preguntaAsociada = models.ForeignKey(Pregunta,related_name="preguntaAsociada")


# Create your models here.


import django_filters

class PersonaFilter(django_filters.FilterSet):
    class Meta:
        model = Persona
        fields = ['apeNombre', 'discapacidad', 'nivelAprobado', 'motivosAbandono', 
        		'oficio', 'condicionActividad', 'seccPadron', 'circuPadron', 'partidoPadron']

class ViviendaFilter(django_filters.FilterSet):
    class Meta:
        model = Vivienda
        fields = ['barrio', 'calle', 'tipoVivienda', 'tenencia', 'servicio', 'banio', 'departamento', 'municipio', 'localidad']


#############################
"""Clase que no se guarda, se usa solo para mostrar"""

"""
class PersonaPatoca(models.Model):
	apeNombre = models.CharField(max_length=100)
	dni = models.CharField(max_length=30)
	fechaNac = models.DateField(default=datetime.now)
	sexo = models.CharField(max_length=10)
	telefono = models.CharField(max_length=20,null=True, blank=True)
	correo = models.CharField(max_length=75,null=True, blank=True)
	vivienda = models.ForeignKey(Vivienda,related_name="vivienda",null=True, blank=True)
	cobertura = models.ForeignKey(CoberturaSalud,related_name="cobertura",null=True, blank=True)
	discapacidad = models.ForeignKey(Discapacidad,related_name="discapacidad",null=True, blank=True)
	nivelAprobado = models.ForeignKey(NivelAprobado,related_name="nivelAprobado",null=True, blank=True)
	motivosAbandono = models.ForeignKey(MotivosAbandono,related_name="motivosAbandono",null=True, blank=True)
	oficio = models.ForeignKey(Oficio,related_name="oficio",null=True, blank=True)
	condicionActividad = models.ForeignKey(CondicionActividad,related_name="condicionActividad",null=True, blank=True)
	domicilioPadron = models.CharField(max_length=300, null=True, blank=True)
    analfPadron = models.CharField(max_length=3, null=True, blank=True)
    seccPadron = models.IntegerField()
    circuPadron = models.IntegerField()
    mesaPadron = models.IntegerField()
    partidoPadron = models.CharField(max_length=100, null=True, blank=True)
"""