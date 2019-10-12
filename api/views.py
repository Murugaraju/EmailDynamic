from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
#Just to check
# For mail related
from django.core import mail
from django.core.mail.backends.smtp import EmailBackend


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


@api_view(['post'])
def test_alertmail(request):
    print("came in test_alertmail")
    if len(AlertMailModel.objects.all()) == 0:
        return Response({"SMPT settings record not exist" :["Try record smpt and reciepient details"]})
    return Response("working")

def send_mail(subject, contact_list, body):

    try:
        mailob=AlertMailModel.objects.first()
        
        con = mail.get_connection(host=mailob.host_smtpaddress,port=587,fail_silently=False)
        con.open()
        print('Django connected to the SMTP server')
        


        host = 'smtp.gmail.com'
        host_user = 'info.temporary.dev@gmail.com'
        host_pass = 'demo123456'
        host_port = 587

        mail_obj = EmailBackend(
            host=host,
            port=host_port,
            password=host_pass,
            username=host_user,
            use_tls=True,
            timeout=10
        )

        msg = mail.EmailMessage(
            subject=subject,
            body=body,
            from_email=host_user,
            to=[contact_list],
            connection=con,
        )
        mail_obj.send_messages([msg])
        print('Message has been sent.')

        mail_obj.close()
        print('SMTP server closed')
        return True

    except Exception as _error:
        print('Error in sending mail >> {}'.format(_error))
        return False