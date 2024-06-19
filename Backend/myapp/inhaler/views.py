from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from .models import inhaler
from .serializers import InhalerSerializer

class InhalerView(APIView):
    
    def post(self,request):
        serializer=InhalerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        obj=inhaler.objects.all()
        serializer=InhalerSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class UserByName(APIView):
    def get(self,request,username):
        try:
            obj=inhaler.objects.get(username=username)
            serializer=InhalerSerializer(obj)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except inhaler.DoesNotExist:
            message={"message":"Not Found"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
    
    
        

