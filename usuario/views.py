from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from usuario.models import Usuario
from usuario.api.serializers import UsuarioSerializer
# Create your views here.

@csrf_exempt
def usuarioApi(request, id=None):
    if request.method == 'GET':
        if id == None:
            usuario = Usuario.objects.all().order_by('nome')
            usuario_serializer = UsuarioSerializer(usuario, many=True)
            return JsonResponse(usuario_serializer.data, safe=False)
        try:
            usuario = Usuario.objects.get(id=id)
            usuario_serializer = UsuarioSerializer(usuario)
            return JsonResponse(usuario_serializer.data, safe=False)
        except Usuario.DoesNotExist:
            return JsonResponse("Usuário não encontrado", status=404)
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

def usuarioById(id_usuario, request):
    print ('id_usuario nova func ', id_usuario)
    usuario = Usuario.objects.get(id=id_usuario)
    usuario_serializer = UsuarioSerializer(usuario)
    return JsonResponse(usuario_serializer.data, safe=False)
