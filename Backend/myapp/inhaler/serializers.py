from rest_framework import serializers
from .models import inhaler

class InhalerSerializer(serializers.ModelSerializer):
    class Meta:
        model=inhaler
        fields='__all__'