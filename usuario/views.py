from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from usuario.models import Usuario
from usuario.api.serializers import UsuarioSerializer
# Create your views here.

@csrf_exempt
def usuarioApi(request, id=0):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuario, many=True)
        return JsonResponse(usuario_serializer.data, safe=False)
    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar!", safe=False)
    elif request.method == 'PUT':
        usuario_data = JSONParser().parse(request)
        usuario = Usuario.objects.get(id=usuario_data['id'])
        usuario_serializer = UsuarioSerializer(usuario, data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Atualizado com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar!", safe=False)
    elif request.method == 'DELETE':
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        return JsonResponse("Deletado com sucesso!", safe=False)
