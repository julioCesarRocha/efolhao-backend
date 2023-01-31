from rest_framework import viewsets
from respiracao.api import serializers
from respiracao import models 

class RespiracaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RespiracaoSerializer
    queryset = models.Respiracao.objects.all()