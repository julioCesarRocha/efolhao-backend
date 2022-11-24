from django.db import models
from uuid import uuid4
# Create your models here.

class Usuario(models.Model) :
    id_usuario = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    data_criacao = models.DateField(auto_now_add=True)
    perfil = models.CharField(max_length=100)