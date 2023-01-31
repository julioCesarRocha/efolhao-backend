from rest_framework import serializers
from respiracao import models

class RespiracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Respiracao
        fields = '__all__'