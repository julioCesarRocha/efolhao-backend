from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from sinaisvitais.models import SinaisVitais
from sinaisvitais.api.serializers import SinaisVitaisSerializer
# Create your views here.

@csrf_exempt
def sinaisVitaisApi(request, id=0):
    # criar tratamento de requisicao GET
    if request.method == 'GET':
        sinaisvitais = SinaisVitais.objects.all()
        sinaisvitais_serializer = SinaisVitaisSerializer(sinaisvitais, many=True)
        return JsonResponse(sinaisvitais_serializer.data, safe=False)
    elif request.method == 'POST':
        sinaisvitais_data = JSONParser().parse(request)
        sinaisvitais_serializer = SinaisVitaisSerializer(data=sinaisvitais_data)
        if sinaisvitais_serializer.is_valid():
            sinaisvitais_serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar!", safe=False)
    elif request.method == 'PUT':
        sinaisvitais_data = JSONParser().parse(request)
        sinaisvitais = SinaisVitais.objects.get(id_sinal_vital=sinaisvitais_data['id_sinal_vital'])
        sinaisvitais_serializer = SinaisVitaisSerializer(sinaisvitais, data=sinaisvitais_data)
        if sinaisvitais_serializer.is_valid():
            sinaisvitais_serializer.save()
            return JsonResponse("Atualizado com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar!", safe=False)
    elif request.method == 'DELETE':
        sinaisvitais = SinaisVitais.objects.get(id_sinal_vital=id)
        sinaisvitais.delete()
        return JsonResponse("Deletado com sucesso!", safe=False)

