from django.contrib.auth.models import User, Group
from web.models import TipoVivienda, Vivienda , Tenencia
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

class ViviendaSerializer(serializers.ModelSerializer):
	tipoVivienda = TipoViviendaSerializer(many=False)
	tenencia = serializers.PrimaryKeyRelatedField(many=False)
	class Meta:
		model = Vivienda
		fields = ('barrio','calle','numero','tipoVivienda','tenencia')