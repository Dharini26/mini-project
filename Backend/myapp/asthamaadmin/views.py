from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import asthamaadmin
from .serializers import AsthamaAdminSerializer

class adminLoginView(APIView):
    queryset=asthamaadmin.objects.all()
    serializer=AsthamaAdminSerializer
    
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        user=asthamaadmin.objects.filter(username=username,password=password).first()

        if user:
            return Response({"message":"Login Successfully"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"Invalid credentials"},status=status.HTTP_400_BAD_REQUEST)