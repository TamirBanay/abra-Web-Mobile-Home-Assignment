from django.conf import settings
from django.db import models
from django.utils import timezone

class Massage(models.Model):
    MassageId = models.AutoField(primary_key=True)
    Sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ReceiverMail = models.CharField(max_length=200,  null=False, blank=True)
    Message= models.CharField(max_length=200,  null=True, blank=True)
    Subject= models.CharField(max_length=100,  null=True, blank=True)
    CreationDate=  models.DateTimeField(default=timezone.now)
    