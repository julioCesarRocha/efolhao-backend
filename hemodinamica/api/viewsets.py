from rest_framework import viewsets
from hemodinamica.api import serializers
from hemodinamica import models 

class HemodinamicaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HemodinamicaSerializer
    queryset = models.Hemodinamica.objects.all()