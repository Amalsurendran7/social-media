from django.db import models
from Rduser.models import *
# Create your models here.
class message_model(models.Model):
    room=models.CharField(max_length=100)
    sender=models.CharField(max_length=100,default=False)
    receiver=models.CharField(max_length=100,default=False)
    


class Messages(models.Model):
 user=models.CharField(max_length=100)
 content=models.TextField()
 room_name=models.ForeignKey(message_model,on_delete=models.CASCADE,related_name="messages")
