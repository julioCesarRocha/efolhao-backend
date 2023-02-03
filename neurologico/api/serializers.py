from rest_framework import serializers
from neurologico import models

class NeurologicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Neurologico
        fields = '__all__'