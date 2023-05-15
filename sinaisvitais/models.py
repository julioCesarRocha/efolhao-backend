from django.db import models
from uuid import uuid4
# import matplotlib.pyplot as plt
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import SinaisVitais

class SinaisVitais(models.Model) :
    id_sinal_vital = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2)
    frequencia_respiratoria = models.IntegerField()
    saturacao = models.IntegerField()
    frequencia_cardiaca = models.IntegerField()
    pa_sistolica = models.DecimalField(max_digits=6, decimal_places=2)
    pa_diastolica = models.DecimalField(max_digits=6, decimal_places=2)
    pa_media = models.DecimalField(max_digits=6, decimal_places=2)
    data_criacao = models.DateField(auto_now_add=True)

def get_sinais_vitais(cls, id):
        try:
            return cls.objects.get(id_sinal_vital=id)
        except cls.DoesNotExist:
            return None

# class PlotSinaisVitais(APIView):

#     def get(self, request, id_sinal_vital):
#         sinais_vitais = SinaisVitais.objects.filter(id_sinal_vital=id_sinal_vital).order_by('data_criacao')
#         temperatura = [sv.temperatura for sv in sinais_vitais]
#         freq_resp = [sv.frequencia_respiratoria for sv in sinais_vitais]
#         saturacao = [sv.saturacao for sv in sinais_vitais]
#         freq_card = [sv.frequencia_cardiaca for sv in sinais_vitais]
#         pa_sist = [sv.pa_sistolica for sv in sinais_vitais]
#         pa_diast = [sv.pa_diastolica for sv in sinais_vitais]
#         pa_media = [sv.pa_media for sv in sinais_vitais]
#         datas = [str(sv.data_criacao) for sv in sinais_vitais]
#         fig, axs = plt.subplots(7, 1, figsize=(12, 12))
#         axs[0].plot(datas, temperatura, 'ro-')
#         axs[0].set_title('Temperatura')
#         axs[0].set_xlabel('Data')
#         axs[0].set_ylabel('Temperatura (ºC)')
#         axs[1].plot(datas, freq_resp, 'bo-')
#         axs[1].set_title('Frequência Respiratória')
#         axs[1].set_xlabel('Data')
#         axs[1].set_ylabel('Frequência Respiratória (ipm)')
#         axs[2].plot(datas, saturacao, 'go-')
#         axs[2].set_title('Saturação')
#         axs[2].set_xlabel('Data')
#         axs[2].set_ylabel('Saturação (%)')
#         axs[3].plot(datas, freq_card, 'co-')
#         axs[3].set_title('Frequência Cardíaca')
#         axs[3].set_xlabel('Data')
#         axs[3].set_ylabel('Frequência Cardíaca (bpm)')
#         axs[4].plot(datas, pa_sist, 'mo-')
#         axs[4].set_title('Pressão Arterial Sistólica')
#         axs[4].set_xlabel('Data')
#         axs[4].set_ylabel('Pressão Arterial Sistólica (mmHg)')
#         axs[5].plot(datas, pa_diast, 'yo-')
#         axs[5].set_title('Pressão Arterial Diastólica')
#         axs[5].set_xlabel('Data')
#         axs[5].set_ylabel('Pressão Arterial Diastólica (mmHg)')
#         axs[6].plot(datas, pa_media, 'ko-')
#         axs[6].set_title('Pressão Arterial Média')
#         axs[6].set_xlabel('Data')
#         axs[6].set_ylabel('Pressão Arterial Média (mmHg)')
#         plt.tight_layout()
#         plt.savefig('sinais_vitais.png')

