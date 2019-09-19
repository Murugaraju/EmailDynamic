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
class AlertMailDetail(APIView):
    def get_object(self,pk):
        try:
            return AlertMail.objects.get(pk=pk)
        except AlertMail.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        alertmailob=self.get_object(pk)
        serializer=AlertMailSerializer(alertmailob)
        return Response(serializer.data)
    def patch(self,request,pk):
        alertmailob=self.get_object(pk)
        serializer=AlertMailSerializer(alertmailob,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        alertmailob = self.get_object(pk)
        alertmailob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

