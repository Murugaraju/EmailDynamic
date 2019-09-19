from rest_framework import serializers
from .models import *

class AlertMailSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    receipient_mail = serializers.EmailField()
    host_mail = serializers.EmailField()
    host_smtpaddress = serializers.CharField(max_length=25)
    def create(self, validated_data):
        return AlertMail.objects.create(**validated_data)
    def update(self, instance, validated_data):
        print("printing validated_data ----->",validated_data)
        instance.receipient_mail = validated_data.get('receipient_mail', instance.receipient_mail)
        instance.host_mail = validated_data.get('host_mail', instance.host_mail)
        instance.host_smtpaddress = validated_data.get('host_smtpaddress', instance.host_smtpaddress)
        print("I am in serializer", instance, type(instance))
        print(instance.save())
        print("asfasdf---->",instance.receipient_mail)
        return instance
