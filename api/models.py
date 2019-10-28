from django.db import models

# Create your models here.
class AlertMailModel(models.Model):
    receipient_mail = models.EmailField()
    host_mail = models.EmailField()
    host_smtpaddress = models.CharField(max_length=25)
    mail_host_password = models.CharField(max_length=200)
    use_tls=models.BooleanField(default=False)
    port=models.CharField(max_length=3,default=25)
    
