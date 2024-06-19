from rest_framework import serializers
from .models import asthamaadmin

class AsthamaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=asthamaadmin
        fields='__all__'