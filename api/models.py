from django.db import models

# Create your models here.
class AlertMailModel(models.Model):
    receipient_mail = models.EmailField(unique=True)
    host_mail = models.EmailField(unique=True)
    host_smtpaddress = models.CharField(max_length=25)
    mail_host_password = models.CharField(max_length=200)
    
