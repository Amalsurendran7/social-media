from django.db import models
from Rduser.models import *

# Create your models here.
class Group_model(models.Model):
  
   group_name=models.CharField(max_length=100)
   description=models.TextField()
   admin=models.CharField(max_length=100,default=False)
   members_count=models.IntegerField(default=False)
   user=models.ForeignKey(customer,on_delete=models.CASCADE,related_name="joined_group",null=True)


class group_members(models.Model):
    username=models.CharField(max_length=100)
    group=models.ForeignKey(Group_model,on_delete=models.CASCADE,related_name="group_member",null=True)


  


class G_Posts(models.Model):
    file = models.FileField(upload_to='images',null=True)
   
    caption=models.TextField(default=False)
   
    group=models.ForeignKey(Group_model,on_delete=models.CASCADE,related_name="post_to_group",null=True)
    user=models.ForeignKey(customer,on_delete=models.CASCADE,related_name="group_post",null=True)
 
    reported=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    banned=models.BooleanField(default=False)
    likes_for_post=models.IntegerField(default=0)

class G_Likes(models.Model):
    user=models.CharField(max_length=100)
    post=models.ForeignKey(G_Posts,on_delete=models.CASCADE)


class post_user(models.Model):
    username=models.CharField(max_length=150,default=None,null=True)
    verify_request=models.BooleanField(default=False)
    verified=models.BooleanField(default=False)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    reported=models.BooleanField(default=False)
    email_verified=models.BooleanField(default=False)
    post=models.ForeignKey(G_Posts,on_delete=models.CASCADE,related_name="posted_by")
    followers=models.IntegerField(default=False)
    following=models.IntegerField(default=False)
 
    online=models.BooleanField(default=False)
    profile_pic=models.FileField(upload_to='images',null=True)
    string_pic=models.CharField(max_length=100,default=False)
    password=models.CharField(max_length=150)
    otp=models.CharField(max_length=150,null=True,blank=True)



class G_Comments(models.Model):
    comment=models.TextField()  
    user=models.CharField(max_length=100)
    post=models.ForeignKey(G_Posts,on_delete=models.CASCADE,related_name="comment_for") 
    prof=models.CharField(max_length=100,default=False)


