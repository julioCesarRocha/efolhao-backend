from django.db import models
from uuid import uuid4

class Respiracao(models.Model) :
    id_dado_respiratorio = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    modo_esp = models.BooleanField()
    modo_vm = models.BooleanField()
    fi02 = models.DecimalField(max_digits=3, decimal_places=1)
    peep = models.DecimalField(max_digits=3, decimal_places=1)
    p_pico = models.IntegerField()
    pet_co2 = models.IntegerField()
    pressao_cuff = models.BooleanField()