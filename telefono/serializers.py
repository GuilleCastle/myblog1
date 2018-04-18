from rest_framework import serializers
from telefono.models import Grupo, Favoritos, Contacto, Correo, Telefono, Tipo_telefono

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ('nombre','descripcion')

class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = ('__all__')

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ('nombre','apellido','grupo','favorito')

class CorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = ('correo', 'contacto')

class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = ('telefono', 'contacto')

class Tipo_telefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_telefono
        fields = ('descripcion', 'telefono')
    