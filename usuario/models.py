from django.db import models
from uuid import uuid4
# Create your models here.

class Usuario(models.Model) :
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=225)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=200, null=True, blank=True)
    senha = models.CharField(max_length=200, null=True, blank=True)
    data_criacao = models.DateField(auto_now_add=True)
    perfil = models.CharField(max_length=100, null=True, blank=True)
    peso = models.FloatField(default=0.0)
    reg = models.CharField(max_length=100, blank=True, default='')
    convenio = models.CharField(max_length=225, blank=True, default='')
    leito = models.CharField(max_length=100, blank=True, default='')

