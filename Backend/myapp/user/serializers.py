from rest_framework import serializers
from .models import asthamauser

class AsthamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=asthamauser
        fields='__all__'