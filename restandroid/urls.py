from django.conf.urls import patterns, include, url
from rest_framework import routers
from web.views import UserViewSet, GroupViewSet, TipoViviendaViewSet, ViviendaViewSet, TenenciaViewSet
from web import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tiposvivienda', views.TipoViviendaViewSet)
router.register(r'viviendas', views.ViviendaViewSet)
router.register(r'tenencias', views.TenenciaViewSet)
router.register(r'sericios', views.ServicioViewSet)
router.register(r'banios', views.BanioViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)
router.register(r'municipios', views.MunicipioViewSet)
router.register(r'localidades', views.LocalidadViewSet)
router.register(r'coberturas', views.CoberturaSaludViewSet)
router.register(r'discapacidades', views.DiscapacidadViewSet)
router.register(r'motivosabandono', views.MotivosAbandonoViewSet)
router.register(r'oficios', views.OficioViewSet)
router.register(r'condicionactividad', views.CondicionActividadViewSet)
router.register(r'personas', views.PersonaViewSet)
router.register(r'encuestas', views.EncuestaViewSet)
router.register(r'preguntas', views.PreguntaViewSet)
router.register(r'respuestas', views.RespuestaViewSet)
router.register(r'estadosalud', views.EstadoSaludViewSet)
router.register(r'viviendas2', views.Vivienda2ViewSet)
router.register(r'preguntas2', views.Pregunta2ViewSet)
router.register(r'respuestas2', views.Respuesta2ViewSet)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restandroid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^index/', 'web.views.index'),
    url(r'^login/', 'web.views.login'),
    url(r'^lista_viviendas/', 'web.views.lista_viviendas'),
    url(r'^lista_personas/', 'web.views.lista_personas'),
    url(r'^vivienda_integrantes/(\d+)/$', 'web.views.vivienda_integrantes'),
)
