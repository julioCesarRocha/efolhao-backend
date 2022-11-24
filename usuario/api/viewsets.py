from rest_framework import viewsets
from usuario.api import serializers
from usuario import models 

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    queryset = models.Usuario.objects.all()