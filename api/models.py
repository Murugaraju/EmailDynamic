from django.db import models

# Create your models here.
class AlertMail(models.Model):
    receipient_mail = models.EmailField(unique=True)
    host_mail = models.EmailField(unique=True)
    host_smtpaddress = models.CharField(max_length=25)
    
