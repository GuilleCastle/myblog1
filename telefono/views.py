from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from telefono.models import (Grupo, Favoritos, 
Contacto, Correo, Telefono, Tipo_telefono)
from telefono.serializers import (GrupoSerializer, Tipo_telefonoSerializer, 
FavoritosSerializer, ContactoSerializer, 
CorreoSerializer, TelefonoSerializer)
from rest_framework import generics 
from rest_framework.permissions import IsAdminUser

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#class GrupoDetail(generics.RetrieveUpdateDestroyAPIView):
 #   queryset = Grupo.objects.all()
  #  serializer_class = GrupoSerializer



@csrf_exempt
def grupo_list(request):
    if request.method == 'GET':
        queryset = Grupo.objects.all()
        serializer = GrupoSerializer(queryset, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GrupoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def grupo_detail(request, pk):
    try:
        grupo = Grupo.objects.get(pk=pk)
    except Grupo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GrupoSerializer(grupo)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GrupoSerializer(grupo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        grupo.delete()
        return HttpResponse(status=204)

    
@csrf_exempt
def favoritos_list(request):
    if request.method == 'GET':
        queryset = Favoritos.objects.all()
        serializer = FavoritosSerializer(queryset, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FavoritosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def favoritos_detail(request, pk):
    try:
        favorito = Favoritos.objects.get(pk=pk)
    except Favoritos.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FavoritosSerializer(favorito)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FavoritosSerializer(favorito, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        favorito.delete()
        return HttpResponse(status=204)


@csrf_exempt
def contacto_list(request):
    if request.method == 'GET':
        queryset = Contacto.objects.all()
        serializer = ContactoSerializer(queryset, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def contacto_detail(request, pk):
    try:
        contacto = Contacto.objects.get(pk=pk)
    except Contacto.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ContactoSerializer(contacto)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactoSerializer(contacto, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        contacto.delete()
        return HttpResponse(status=204)


@csrf_exempt
def correo_list(request):
    if request.method == 'GET':
        queryset = Correo.objects.all()
        serializer = CorreoSerializer(queryset, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CorreoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def correo_detail(request, pk):
    try:
        correo = Correo.objects.get(pk=pk)
    except Correo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CorreoSerializer(correo)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CorreoSerializer(correo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        correo.delete()
        return HttpResponse(status=204)


@csrf_exempt
def telefono_list(request):
    if request.method == 'GET':
        queryset = Telefono.objects.all()
        serializer = TelefonoSerializer(queryset, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TelefonoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def telefono_detail(request, pk):
    try:
        telefono = Telefono.objects.get(pk=pk)
    except Telefono.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TelefonoSerializer(telefono)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TelefonoSerializer(telefono, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        telefono.delete()
        return HttpResponse(status=204)


@csrf_exempt
def tipo_telefono_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        queryset = Tipo_telefono.objects.all()
        serializer = Tipo_telefonoSerializer(queryset, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Tipo_telefonoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def tipo_telefono_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        tipo = Tipo_telefono.objects.get(pk=pk)
    except Tipo_telefono.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Tipo_telefonoSerializer(tipo)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Tipo_telefonoSerializer(tipo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        tipo.delete()
        return HttpResponse(status=204)
