from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from .models import asthamauser
from .serializers import AsthamaUserSerializer

class userRegisterView(APIView):
    
    def post(self,request):
        serializer=AsthamaUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        obj=asthamauser.objects.all()
        serializer=AsthamaUserSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class UserByName(APIView):
    def get(self,request,username):
        try:
            obj=asthamauser.objects.get(username=username)
            serializer=AsthamaUserSerializer(obj)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except asthamauser.DoesNotExist:
            message={"message":"Not Found"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
    
    
class UserLoginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=asthamauser.objects.filter(username=username,password=password)
        
        if user:
            return Response({"message":"Login Successfully"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"Invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
        

class UpdateInhaler(APIView):
    def put(self,request,username):
        try:
            obj=asthamauser.objects.get(username=username)
        except asthamauser.DoesNotExist:
            message={"message":"Not found"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        obj.quantity=obj.quantity - 1
        serializer = AsthamaUserSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class RefillInhaler(APIView):
    def put(self,request,username):
        try:
            obj=asthamauser.objects.get(username=username)
        except asthamauser.DoesNotExist:
            message={"message":"Not found"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        obj.quantity=100
        serializer = AsthamaUserSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        