from rest_framework import serializers
from sinaisvitais import models

class SinaisVitaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SinaisVitais
        fields = '__all__'