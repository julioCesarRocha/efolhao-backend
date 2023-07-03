from django.db import models
from uuid import uuid4
from usuario.models import Usuario

class Hemodinamica(models.Model) :
    id_dado_hemodinamica = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pressao_venosa_central  = models.DecimalField(max_digits=4, decimal_places=1)
    pap = models.DecimalField(max_digits=4, decimal_places=1)
    poap = models.IntegerField()
    ic = models.DecimalField(max_digits=4, decimal_places=1)
    debito_cardiaco = models.DecimalField(max_digits=4, decimal_places=1)
    sv02 = models.IntegerField()
    id_usuario = models.CharField(max_length=350, null=True, blank=True)
    data_criacao = models.DateField(auto_now_add=True)