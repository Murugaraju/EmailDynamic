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
        alertmail = AlertMailModel.objects.all()
        
        if len(alertmail)==0:
            return Response([])
        else:

            serializer =  AlertMailSerializer(alertmail[0])
            data=serializer.data
            # del(data['mail_host_password'])
            return Response(data)
    def post(self,request):
       
        print("printing request post ----->",request.data, type(request.data))
        if len(AlertMailModel.objects.all())!=0:
            return Response({"SMPT Record already exists" : ["Try overriding existing or delete existing one"]},403)
        serializer = AlertMailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data=serializer.data
            del(data['mail_host_password'])
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AlertMailDetail(APIView):
    def get_object(self,pk):
        try:
            return AlertMailModel.objects.get(pk=pk)
        except AlertMail.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        alertmailob=self.get_object(pk)
        serializer=AlertMailSerializer(alertmailob)
        data=serializer.data
        del(data['mail_host_password'])
        return Response(data)
    def patch(self,request,pk):
        alertmailob=self.get_object(pk)
        serializer=AlertMailSerializer(alertmailob,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data=serializer.data
        del(data['mail_host_password'])
        return Response(data)
    def delete(self, request, pk):
        alertmailob = self.get_object(pk)
        alertmailob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

