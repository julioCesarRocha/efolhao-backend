from django.db import models
from uuid import uuid4
# Create your models here.

class Hemodinamica(models.Model) :
    id_dado_hemodinamica = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pressao_venosa_central  = models.DecimalField(max_digits=4, decimal_places=1)
    pap = models.DecimalField(max_digits=4, decimal_places=1)
    poap = models.IntegerField()
    ic = models.BooleanField()
    sv02 = models.IntegerField()
    # id_usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)