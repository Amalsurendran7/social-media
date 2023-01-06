from django.db import models
from django.contrib.auth.models import AbstractUser





class customer(models.Model):
    username=models.CharField(max_length=150,default=None,null=True)
    verify_request=models.BooleanField(default=False)
    verified=models.BooleanField(default=False)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    reported=models.BooleanField(default=False)
    email_verified=models.BooleanField(default=False)
  
    followers=models.IntegerField(default=False)
    following=models.IntegerField(default=False)
 
    online=models.BooleanField(default=False)
    profile_pic=models.FileField(upload_to='frontend/src/post_images',default=False)
    string_pic=models.CharField(max_length=100,default=False)
    password=models.CharField(max_length=150)
    otp=models.CharField(max_length=150,null=True,blank=True)


  