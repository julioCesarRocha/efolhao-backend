from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from neurologico.models import Neurologico
from neurologico.api.serializers import NeurologicoSerializer
# Create your views here.

@csrf_exempt
def neurologicoApi(request, id=0):
    if request.method == 'GET':
        neurologico = Neurologico.objects.all()
        neurologico_serializer = NeurologicoSerializer(neurologico, many=True)
        return JsonResponse(neurologico_serializer.data, safe=False)
    elif request.method == 'POST':
        neurologico_data = JSONParser().parse(request)
        neurologico_serializer = NeurologicoSerializer(data=neurologico_data)
        if neurologico_serializer.is_valid():
            neurologico_serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar!", safe=False)
    elif request.method == 'PUT':
        neurologico_data = JSONParser().parse(request)
        neurologico = Neurologico.objects.get(id=neurologico_data['id'])
        neurologico_serializer = NeurologicoSerializer(neurologico, data=neurologico_data)
        if neurologico_serializer.is_valid():
            neurologico_serializer.save()
            return JsonResponse("Atualizado com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar!", safe=False)
    elif request.method == 'DELETE':
        neurologico = Neurologico.objects.get(id=id)
        neurologico.delete()
        return JsonResponse("Deletado com sucesso!", safe=False)
