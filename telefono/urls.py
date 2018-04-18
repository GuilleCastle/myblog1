from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import SuperHeroeDetail, SuperHeroeList, PublisherDetail, PublisherList
from .views import grupo_list, favoritos_list, contacto_list, correo_list, telefono_list, tipo_telefono_list, grupo_detail, favoritos_detail, contacto_detail, correo_detail, telefono_detail, tipo_telefono_detail 

urlpatterns = [
    url(r'^grupo/', grupo_list, name="grupo"),
    url(r'^favoritos/', favoritos_list, name="favoritos"),
    url(r'^contacto/', contacto_list, name="contacto"),
    url(r'^correo/', correo_list, name="correo"),
    url(r'^telefono/', telefono_list, name="telefono"),
    url(r'^tipo_telefono/', tipo_telefono_list, name="tipo_telefono"),
    url(r'^gruposeleccionar/(?P<pk>\d+)/', grupo_detail, name="gruponumero"),
    url(r'^favoritosseleccionar/(?P<pk>\d+)/', favoritos_detail, name="favoritosnumero"),
    url(r'^contactoseleccionar/(?P<pk>\d+)/', contacto_detail, name="contactonumero"),
    url(r'^correoseleccionar/(?P<pk>\d+)/', correo_detail, name="correonumero"),
    url(r'^telefonoseleccionar/(?P<pk>\d+)/', telefono_detail, name="telefononumero"),
    url(r'^tipo_telefonoseleccionar/(?P<pk>\d+)/', tipo_telefono_detail, name="tipogruponumero"),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)