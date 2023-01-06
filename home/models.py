from django.db import models
from Rduser.models import *
from django.core.validators import FileExtensionValidator

# Create your models here.

class Posts(models.Model):
    file = models.FileField(upload_to='frontend/src/post_images')
    # video = models.FileField(upload_to='frontend/src/post_videos',null=True,
    # validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    caption=models.TextField(default=False)
   
    user=models.ForeignKey(customer,on_delete=models.CASCADE,related_name="post_by",null=True)
    reported=models.BooleanField(default=False)
    reason=models.TextField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    banned=models.BooleanField(default=False)
    likes_for_post=models.IntegerField(default=0)

class Likes(models.Model):
    user=models.CharField(max_length=100)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)



class Calls_video(models.Model):
    username=models.ForeignKey(customer,on_delete=models.CASCADE,related_name="calls_for") 
    caller_name=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    


class Comments(models.Model):
    comment=models.TextField()  
    user=models.CharField(max_length=100)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="comment_for") 
    prof=models.CharField(max_length=100,default=False)


class reply(models.Model):
    reply=models.TextField()  
    user=models.CharField(max_length=100)
    comment=models.ForeignKey(Comments,on_delete=models.CASCADE,related_name="reply_of") 

class followers(models.Model):
        followed_user=models.ForeignKey(customer,on_delete=models.CASCADE,related_name="user_followed")
        follower=models.CharField(max_length=100)

class Status_model(models.Model):
    status=models.FileField(upload_to='frontend/src/post_images')
    user=models.ForeignKey(customer,on_delete=models.CASCADE,related_name="status_by",null=True)
    # created_at = models.DateField(auto_now_add=True)
         

    
    


