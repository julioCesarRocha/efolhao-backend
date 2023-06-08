from django.db import models
from uuid import uuid4
from usuario.models import Usuario

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
    # id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    id_usuario = models.UUIDField(null=True, blank=True)

def get_sinais_vitais(id):
    try:
        return SinaisVitais.objects.filter(id_usuario=id)
    except SinaisVitais.DoesNotExist:
        return None
