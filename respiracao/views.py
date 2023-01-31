from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from respiracao.models import Respiracao
from respiracao.api.serializers import RespiracaoSerializer

@csrf_exempt
def respiracaoApi(request, id=0):
    if request.method == 'GET':
        respiracao = Respiracao.objects.all()
        respiracao_serializer = RespiracaoSerializer(respiracao, many=True)
        return JsonResponse(respiracao_serializer.data, safe=False)
    elif request.method == 'POST':
        respiracao_data = JSONParser().parse(request)
        respiracao_serializer = RespiracaoSerializer(data=respiracao_data)
        if respiracao_serializer.is_valid():
            respiracao_serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar!", safe=False)
    elif request.method == 'PUT':
        respiracao_data = JSONParser().parse(request)
        respiracao = Respiracao.objects.get(id_respiracao=respiracao_data['id_respiracao'])
        respiracao_serializer = RespiracaoSerializer(respiracao, data=respiracao_data)
        if respiracao_serializer.is_valid():
            respiracao_serializer.save()
            return JsonResponse("Atualizado com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar!", safe=False)
    elif request.method == 'DELETE':
        respiracao = Respiracao.objects.get(id_respiracao=id)
        respiracao.delete()
        return JsonResponse("Deletado com sucesso!", safe=False)