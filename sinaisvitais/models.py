from django.db import models
from uuid import uuid4

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

