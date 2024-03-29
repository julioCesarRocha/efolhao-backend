from django.db import models
from uuid import uuid4
from usuario.models import Usuario

# Create your models here.

class Neurologico(models.Model) :
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    glasgow = models.IntegerField()
    pupilas = models.CharField(max_length=25)
    sas = models.CharField(max_length=200)  
    dor = models.IntegerField()
    pic = models.CharField(max_length=200)
    sj02 = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)
    id_usuario = models.CharField(max_length=350, null=True, blank=True)
    abertura_ocular = models.IntegerField(null=True, blank=True)
    resposta_verbal = models.IntegerField(null=True, blank=True)
    resposta_motora = models.IntegerField(null=True, blank=True)
