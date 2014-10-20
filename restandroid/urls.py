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

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restandroid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
