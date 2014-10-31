from django.db import models

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

class Banio(models.Model):
	si = models.BooleanField(default=False)
	no = models.BooleanField(default=False)

class Vivienda(models.Model):
	barrio = models.CharField(max_length=100)
	calle = models.CharField(max_length=100)
	numero = models.CharField(max_length=20)
	piso = models.CharField(max_length=20,blank=True)
	dpto = models.CharField(max_length=10,blank=True)
	tipoVivienda = models.ForeignKey(TipoVivienda,related_name='tipoVivienda')
	tenencia = models.ForeignKey(Tenencia,related_name="tenencia")
	servicio = models.ForeignKey(Servicio,related_name="servicio")
	banio = models.ForeignKey(Banio,related_name="banio")
	departamento = models.ForeignKey(Departamento,related_name="departamento")
	municipio = models.ForeignKey(Municipio,related_name="municipio")
	localidad = models.ForeignKey(Localidad,related_name="localidad")

	def __unicode__(self):
		return self.calle

class CoberturaSalud(models.Model):
	nombre = models.CharField(max_length=75)

class Discapacidad(models.Model):
	nombre = models.CharField(max_length=75)

class NivelAprobado(models.Model):
	nombre = models.CharField(max_length=75)

class MotivosAbandono(models.Model):
	nombre = models.CharField(max_length=75)

class Oficio(models.Model):
	nombre = models.CharField(max_length=75)

class CondicionActividad(models.Model):
	nombre = models.CharField(max_length=75)

class Persona(models.Model):
	apeNombre = models.CharField(max_length=100)
	dni = models.CharField(max_length=30)
	fechaNac = models.DateField()
	sexo = models.CharField(max_length=10)
	telefono = models.CharField(max_length=20)
	correo = models.CharField(max_length=75,blank=True)
	vivienda = models.ForeignKey(Vivienda,related_name="vivienda")
	cobertura = models.ForeignKey(CoberturaSalud,related_name="cobertura")
	discapacidad = models.ForeignKey(Discapacidad,related_name="discapacidad")
	nivelAprobado = models.ForeignKey(NivelAprobado,related_name="nivelAprobado")
	motivosAbandono = models.ForeignKey(MotivosAbandono,related_name="motivosAbandono")
	oficio = models.ForeignKey(Oficio,related_name="oficio")
	condicionActividad = models.ForeignKey(CondicionActividad,related_name="condicionActividad")

class Encuesta(models.Model):
	pregunta = models.CharField(max_length=350)
	respuestaSi = models.IntegerField()
	respuestaNo = models.IntegerField()
	respuestaNoSabe = models.IntegerField()
	fecha = models.DateField()



# Create your models here.
