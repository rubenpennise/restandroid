from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from web.serializers import *
from web.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TipoViviendaViewSet(viewsets.ModelViewSet):
    queryset = TipoVivienda.objects.all()
    serializer_class = TipoViviendaSerializer

class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer

class TenenciaViewSet(viewsets.ModelViewSet):
    queryset = Tenencia.objects.all()
    serializer_class = TenenciaSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class BanioViewSet(viewsets.ModelViewSet):
    queryset = Banio.objects.all()
    serializer_class = BanioSerializer

class CoberturaSaludViewSet(viewsets.ModelViewSet):
    queryset = CoberturaSalud.objects.all()
    serializer_class = CoberturaSaludSerializer

class DiscapacidadViewSet(viewsets.ModelViewSet):
    queryset = Discapacidad.objects.all()
    serializer_class = DiscapacidadSerializer

class MotivosAbandonoViewSet(viewsets.ModelViewSet):
    queryset = MotivosAbandono.objects.all()
    serializer_class = MotivosAbandonoSerializer

class OficioViewSet(viewsets.ModelViewSet):
    queryset = Oficio.objects.all()
    serializer_class = OficioSerializer

class CondicionActividadViewSet(viewsets.ModelViewSet):
    queryset = CondicionActividad.objects.all()
    serializer_class = CondicionActividadSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

# Create your views here.
