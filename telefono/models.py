from django.db import models

# Create your models here.

class Grupo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, default='', null=False)
    descripcion = models.CharField(max_length=100, blank=True, default='', null=False)

class Favoritos(models.Model):
    descripcion = models.CharField(max_length=100, blank=True, default='', null=False)

class Contacto(models.Model):
    nombre = models.CharField(max_length=100, blank=True, default='', null=False) 
    apellido = models.CharField(max_length=100, blank=True, default='', null=False)
    #llaves 
    grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE, null=True)
    favorito = models.ForeignKey('Favoritos', on_delete=models.CASCADE, null=True)

class Correo(models.Model):
    correo = models.CharField(max_length=100, blank=True, default='', null=False)
    #llave
    contacto = models.ForeignKey('Contacto', on_delete=models.CASCADE, null=False)


class Telefono(models.Model):
    telefono = models.CharField(max_length=15, blank=True, default='', null=False)
    #llave
    contacto = models.ForeignKey('Contacto', on_delete=models.CASCADE, null=False)


class Tipo_telefono(models.Model):
    descripcion = models.CharField(max_length=100, blank=True, default='', null=False)
    #llave
    telefono = models.ForeignKey('Telefono', on_delete=models.CASCADE, null=False)

