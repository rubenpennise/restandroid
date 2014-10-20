from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from web.serializers import UserSerializer, GroupSerializer, TipoViviendaSerializer, ViviendaSerializer, TenenciaSerializer
from web.models import TipoVivienda, Vivienda, Tenencia


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

# Create your views here.
