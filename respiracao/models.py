from django.db import models
from uuid import uuid4
from usuario.models import Usuario

class Respiracao(models.Model) :
    id_dado_respiratorio = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    modo_esp = models.CharField(max_length=255)
    modo_vm = models.CharField(max_length=255)
    fi02 = models.IntegerField()
    peep = models.DecimalField(max_digits=3, decimal_places=1)
    p_pico = models.DecimalField(max_digits=3, decimal_places=1)
    volume_corrente = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)
    # id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    id_usuario = models.CharField(max_length=350, null=True, blank=True)
    # pet_co2 = models.IntegerField()
    # pressao_cuff = models.BooleanField()