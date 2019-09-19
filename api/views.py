from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework import status
# Create your views here.


class AlertMailList(APIView):

    def get(self,request):
        alertmails = AlertMail.objects.all()
        serializer =  AlertMailSerializer(alertmails, many=True)

        return Response(serializer.data)
    def post(self,request):
        print("printing request post ----->",request.data, type(request.data))
        
        serializer = AlertMailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)