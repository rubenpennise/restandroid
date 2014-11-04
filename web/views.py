from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from web.serializers import *
from web.models import *

from django.views.generic import TemplateView
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from rest_framework import status



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

class EncuestaViewSet(viewsets.ModelViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer

    @detail_route(methods=['post'])
    def set_password(self, request, pk=None):
        encuesta = self.get_object()
        print encuesta.pregunta
        serializer = EncuestaSerializer(data=request.DATA)
        if serializer.is_valid():
            encuesta.pregunta=serializer.data['pregunta']
            encuesta.save()
            data={'status': 'encuesta update'}
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

######## Funciones #######



def index(request):

    query = request.GET.get('q', '')
    
    if query:
        qset = (
            Q(apeNombre__icontains=query)
            )
        f = PersonaFilter(request.GET, queryset=Persona.objects.all().order_by('apeNombre').filter(qset))
    else:
        f = PersonaFilter(request.GET, queryset=Persona.objects.all())
    paginator = Paginator(f, 20)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    # If page request (9999) is out of range, deliver last page of results.
    try:
        lista_personas = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista_personas = paginator.page(paginator.num_pages)
    return render_to_response('web/index.html', {'filter': f,
                                                'lista_personas': lista_personas,
                                                }, context_instance=RequestContext(request))

def lista_viviendas(request):


    query = request.GET.get('q', '')
    
    if query:
        f = ViviendaFilter(request.GET, queryset=Vivienda.objects.all().filter(query))
    else:
        f = ViviendaFilter(request.GET, queryset=Vivienda.objects.all())
    paginator = Paginator(f, 20)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    # If page request (9999) is out of range, deliver last page of results.
    try:
        lista_viviendas = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista_viviendas = paginator.page(paginator.num_pages)
    return render_to_response('web/viviendas.html', {'filter': f,
                                                'lista_viviendas': lista_viviendas,
                                                }, context_instance=RequestContext(request))

def vivienda_integrantes(request, vivienda_id):
    vivienda = Vivienda.objects.get(id=vivienda_id)
    lista_personas = Persona.objects.all().filter(vivienda=vivienda)
    return render_to_response('web/vivienda_integrantes.html', {'lista_personas': lista_personas,
                                                'vivienda': vivienda,
                                                }, context_instance=RequestContext(request))
