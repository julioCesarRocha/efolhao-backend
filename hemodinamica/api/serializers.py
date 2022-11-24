from rest_framework import serializers
from hemodinamica import models

class HemodinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hemodinamica
        fields = '__all__'