from rest_framework import viewsets
from neurologico.api import serializers
from neurologico import models 

class NeurologicoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NeurologicoSerializer
    queryset = models.Neurologico.objects.all()