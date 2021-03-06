from django.contrib.auth.models import User, Group
from web.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class TipoViviendaSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoVivienda
		fields = ('nombre',)

class TenenciaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tenencia
		fields = ('nombre',)

class ServicioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servicio
		fields = ('luz','agua','gas','telefono','cloacas')

class DepartamentoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Departamento
		fields = ('nombre',)

class MunicipioSerializer(serializers.ModelSerializer):
	departamento = serializers.PrimaryKeyRelatedField(many=False)
	class Meta:
		model = Municipio
		fields = ('nombre','departamento')

class LocalidadSerializer(serializers.ModelSerializer):
	municipio = serializers.PrimaryKeyRelatedField(many=False)
	class Meta:
		model = Localidad
		fields = ('nombre','municipio')

class BanioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Banio
		fields = ('si','no')

class ViviendaSerializer(serializers.ModelSerializer):
	tipoVivienda = serializers.PrimaryKeyRelatedField(many=False)
	tenencia = serializers.PrimaryKeyRelatedField(many=False)
	servicio = ServicioSerializer(many=False)
	banio = BanioSerializer(many=False)
	departamento = serializers.PrimaryKeyRelatedField(many=False)
	municipio = serializers.PrimaryKeyRelatedField(many=False)
	localidad =serializers.PrimaryKeyRelatedField(many=False)
	class Meta:
		model = Vivienda
		fields = ('barrio','calle','numero','piso','dpto','tipoVivienda','tenencia','cantidadHabitaciones','urgenciasBasicas','departamento','municipio','localidad','servicio','banio')

class CoberturaSaludSerializer(serializers.ModelSerializer):
	class Meta:
		model = CoberturaSalud
		fields =('nombre',)

class DiscapacidadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Discapacidad
		fields =('nombre',)

class NivelAprobadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = NivelAprobado
		fields =('nombre',)

class MotivosAbandonoSerializer(serializers.ModelSerializer):
	class Meta:
		model = MotivosAbandono
		fields =('nombre',)

class OficioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Oficio
		fields =('nombre',)

class CondicionActividadSerializer(serializers.ModelSerializer):
	class Meta:
		model = CondicionActividad
		fields =('nombre',)

class EstadoSaludSerializer(serializers.ModelSerializer):
	class Meta:
		model = EstadoSalud
		fields = ('nombre','descripcion')

class PersonaSerializer(serializers.ModelSerializer):
	vivienda = serializers.PrimaryKeyRelatedField(many=False)
	cobertura = serializers.PrimaryKeyRelatedField(many=False)
	discapacidad = serializers.PrimaryKeyRelatedField(many=False)
	nivelAprobado = serializers.PrimaryKeyRelatedField(many=False)
	motivosAbandono = serializers.PrimaryKeyRelatedField(many=False)
	oficio = serializers.PrimaryKeyRelatedField(many=False)
	condicionActividad = serializers.PrimaryKeyRelatedField(many=False)
	estadoSalud = EstadoSaludSerializer(many=False)
	class Meta:
		model = Persona
		fields = ('apeNombre','dni','fechaNac','sexo','telefono','correo','vivienda','cobertura','discapacidad','nivelAprobado','motivosAbandono','oficio','jefeDeHogar','estadoSalud','condicionActividad')

class EncuestaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Encuesta
		fields = ('id','pregunta','respuestaSi','respuestaSi','respuestaNo','respuestaNoSabe','fecha','codigo')

class PreguntaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pregunta
		fields = ('pregunta','fecha','codigo')

class RespuestaSerializer(serializers.ModelSerializer):
	preguntaAsociada = serializers.PrimaryKeyRelatedField(many=False)
	class Meta:
		model = Respuesta
		fields = ('respuesta','resultado','preguntaAsociada','codigo')

class SaludReproductivaSerializer(serializers.ModelSerializer):
	class Meta:
		model = SaludReproductiva
		fields = ('usoDeAnticonceptivo','tipoDeAnticonceptivo','fechaUltimaMenstruacion','fechaProbableParto','embarazoRiesgoso','lugaresDeControl','tipoDeParto','tipoDeAborto','lugarDeAborto')

class EntornoAmbientalSerializer(serializers.ModelSerializer):
	class Meta:
		model = EntornoAmbiental
		fields = ('ubicacionVilla','ubicacionZonaInundable','existenciaBasural','existenciaCloacas','aguaCorriente','energiaElectrica','gasNatural','cuadraPavimentada','recoleccionResiduos','transportePublico','alumbradoPublico')

class ConsumoAnimalSerializer(serializers.ModelSerializer):
	class Meta:
		model = ConsumoAnimal
		fields = ('aves','conejos','cerdos','ovejasCabras','vacas','otrosAnimales','noCria')

class ConsumoCultivosSerializer(serializers.ModelSerializer):
	class Meta:
		model = ConsumoCultivos
		fields = ('frutales','hortalizas','tuberculos','granos','huerta','otrosCultivos','ninguno')

""" aqui vamos a aplicar otra forma de serializers de modo de evitar el problema
con las claves foraneas a la hora de dar de alta relaciones uno a muchos."""
class Persona2Serializer(serializers.ModelSerializer):
	cobertura = serializers.PrimaryKeyRelatedField(many=False)
	discapacidad = serializers.PrimaryKeyRelatedField(many=False)
	nivelAprobado = serializers.PrimaryKeyRelatedField(many=False)
	motivosAbandono = serializers.PrimaryKeyRelatedField(many=False)
	oficio = serializers.PrimaryKeyRelatedField(many=False)
	condicionActividad = serializers.PrimaryKeyRelatedField(many=False)
	estadoSalud = EstadoSaludSerializer(many=False)
	saludReproductiva = SaludReproductivaSerializer(many=False)
	class Meta:
		model = Persona
		fields = ('apeNombre','dni','fechaNac','sexo','telefono','correo','cobertura','discapacidad','nivelAprobado','motivosAbandono','oficio','jefeDeHogar','estadoSalud','condicionActividad','saludReproductiva')


class Vivienda2Serializer(serializers.ModelSerializer):
	tipoVivienda = serializers.PrimaryKeyRelatedField(many=False)
	tenencia = serializers.PrimaryKeyRelatedField(many=False)
	servicio = ServicioSerializer(many=False)
	banio = BanioSerializer(many=False)
	departamento = serializers.PrimaryKeyRelatedField(many=False)
	municipio = serializers.PrimaryKeyRelatedField(many=False)
	localidad =serializers.PrimaryKeyRelatedField(many=False)
	vivienda = Persona2Serializer(many=True)
	entornoAmbiental = EntornoAmbientalSerializer(many=False)
	consumoAnimal = ConsumoAnimalSerializer(many=False)
	consumoCultivos = ConsumoCultivosSerializer(many=False)
	class Meta:
		model = Vivienda
		fields = ('barrio','calle','numero','piso','dpto','tipoVivienda','tenencia','cantidadHabitaciones','urgenciasBasicas','departamento','municipio','localidad','servicio','banio','vivienda','entornoAmbiental','consumoAnimal','consumoCultivos')

class Respuesta2Serializer(serializers.ModelSerializer):
	class Meta:
		model = Respuesta
		fields = ('respuesta','resultado','codigo')

class Pregunta2Serializer(serializers.ModelSerializer):
	preguntaAsociada = Respuesta2Serializer(many=True)
	class Meta:
		model = Pregunta
		fields = ('pregunta','fecha','codigo','preguntaAsociada')