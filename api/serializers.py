from rest_framework import serializers
from .models import *
from cryptography.fernet import Fernet
from django.conf import settings


#fernet obj
ferobj=Fernet(settings.FERNET_SECRET_KEY)

class AlertMailSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    receipient_mail = serializers.EmailField()
    host_mail = serializers.EmailField()
    host_smtpaddress = serializers.CharField(max_length=25)
    mail_host_password = serializers.CharField(max_length=200, required=True)
    use_tls= serializers.BooleanField(required=True)
    port = serializers.CharField(max_length=3,required=True)
    def create(self, validated_data):
        # host_mail_encry_password
        print("printing validated -------> ", type(validated_data))
        

        validated_data['mail_host_password'] = ferobj.encrypt(validated_data['mail_host_password'].encode()).decode()
        # del(validated_data['password'])
        print("printing**************8",validated_data)
        
        return AlertMailModel.objects.create(**validated_data)
    def update(self, instance, validated_data):
        print("printing validated_data ----->",validated_data, type(validated_data))
        instance.receipient_mail = validated_data.get('receipient_mail', instance.receipient_mail)
        instance.host_mail = validated_data.get('host_mail', instance.host_mail)
        if(validated_data.get('mail_host_password',False)):
            instance.mail_host_password=ferobj.encrypt(validated_data['mail_host_password'].encode()).decode()
            
        instance.host_smtpaddress = validated_data.get('host_smtpaddress', instance.host_smtpaddress)
        instance.port=validated_data.get('port',instance.port)
        # instance.mail_host_password=validated_data.get('mail_host_password',instance.mail_host_password)
        print("I am in serializer", instance, type(instance))
        print(instance.save())
        print("asfasdf---->",instance.receipient_mail)
        return instance
    class Meta:
        fields =['id','receipient_mail','host_mail','host_smtpaddress','use_tls','port']