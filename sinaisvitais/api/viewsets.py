from rest_framework import viewsets
from sinaisvitais.api import serializers
from sinaisvitais import models 

class SinaisVitaisViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SinaisVitaisSerializer
    queryset = models.SinaisVitais.objects.all()