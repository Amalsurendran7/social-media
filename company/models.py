from django.db import models
from Rduser.models import customer

# Create your models here.

class company_info(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    description=models.TextField()
    is_pending=models.BooleanField(default=True)
    declined=models.BooleanField(default=False)
    processing=models.BooleanField(default=False)
    slot=models.CharField(default=False,max_length=70)
    username=models.CharField(default=False,max_length=70)
    CP=models.TextField(default=False)
    problem=models.TextField(default=False)
    proposal=models.TextField(default=False)
    
  
    
