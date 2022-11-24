from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from hemodinamica.models import Hemodinamica
from hemodinamica.api.serializers import HemodinamicaSerializer
# Create your views here.

@csrf_exempt
def hemodinamicaApi(request, id=0):
    if request.method == 'GET':
        hemodinamica = Hemodinamica.objects.all()
        hemodinamica_serializer = HemodinamicaSerializer(hemodinamica, many=True)
        return JsonResponse(hemodinamica_serializer.data, safe=False)
    elif request.method == 'POST':
        hemodinamica_data = JSONParser().parse(request)
        hemodinamica_serializer = HemodinamicaSerializer(data=hemodinamica_data)
        if hemodinamica_serializer.is_valid():
            hemodinamica_serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar!", safe=False)
    elif request.method == 'PUT':
        hemodinamica_data = JSONParser().parse(request)
        hemodinamica = Hemodinamica.objects.get(id_dado_hemodinamica=hemodinamica_data['id_dado_hemodinamica'])
        hemodinamica_serializer = HemodinamicaSerializer(hemodinamica, data=hemodinamica_data)
        if hemodinamica_serializer.is_valid():
            hemodinamica_serializer.save()
            return JsonResponse("Atualizado com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar!", safe=False)
    elif request.method == 'DELETE':
        hemodinamica = Hemodinamica.objects.get(id_dado_hemodinamica=id)
        hemodinamica.delete()
        return JsonResponse("Deletado com sucesso!", safe=False)