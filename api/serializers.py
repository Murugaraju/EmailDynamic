from rest_framework import serializers
from .models import *

class AlertMailSerializer(serializers.Serializer):
    receipient_mail = serializers.EmailField()
    host_mail = serializers.EmailField()
    host_smtpaddress = serializers.CharField(max_length=25)
    def create(self, validated_data):
        return AlertMail.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.receipient_mail = validated_data.get('email', instance.receipient_mail)
        instance.host_mail = validated_data.get('host_mail', instance.host_mail)
        instance.host_smtpaddress = validated_data.get('host_smtpaddress', instance.host_smtpaddress)
        instance.save()
        return instance
