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

class PersonaSerializer(serializers.ModelSerializer):
	vivienda = serializers.PrimaryKeyRelatedField(many=False)
	cobertura = serializers.PrimaryKeyRelatedField(many=False)
	discapacidad = serializers.PrimaryKeyRelatedField(many=False)
	nivelAprobado = serializers.PrimaryKeyRelatedField(many=False)
	motivosAbandono = serializers.PrimaryKeyRelatedField(many=False)
	oficio = serializers.PrimaryKeyRelatedField(many=False)
	condicionActividad = serializers.PrimaryKeyRelatedField(many=False)
	estadoSalud = serializers.PrimaryKeyRelatedField(many=False)
	class Meta:
		model = Persona
		fields = ('apeNombre','dni','fechaNac','sexo','telefono','correo','vivienda','cobertura','discapacidad','nivelAprobado','motivosAbandono','oficio','jefeDeHogar','estadoSalud','infoAdicional','condicionActividad')

class EncuestaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Encuesta
		fields = ('id','pregunta','respuestaSi','respuestaSi','respuestaNo','respuestaNoSabe','fecha')
		