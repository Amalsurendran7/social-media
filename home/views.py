
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework.decorators import api_view
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser
import jwt,datetime
from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponse
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
import json
import uuid
from Rduser.serializers import *
from Rduser.models import *

# Create your views here.


@api_view(['POST'])
def create_post(request):
    print(request.data['name'])
    return Response("hlo")



class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        
       
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data['user'],"data from js")
        me=request.data['user']
        customer_inst=customer.objects.get(username=me)
        kp={"user":customer_inst.id,"file":request.data['file'],"caption":request.data['caption']}
        print(kp)


        
        posts_serializer = PostSerializer(data=kp,partial=True)
        if posts_serializer.is_valid():
            posts_serializer.save()
            
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['POST'])
def current_profile_view(request):
    username=request.data['username']   
    print(username,"my username")
    profile_inst=customer.objects.get(username=username) 
    serializer=UserSerializer(profile_inst,many=False)
    return Response(serializer.data) 

@api_view(['GET'])
def suggestion(request):
    suggested_users=customer.objects.filter(followers__gte=100)   
    serializer=UserSerializer(suggested_users,many=True)
    return Response(serializer.data) 


@api_view(['POST'])
def call_notify(request):
    user_obj=customer.objects.get(username=request.data["receiver"])
    print(user_obj)
    print(user_obj.id)
    serializer=CallSerializer(data={"username":user_obj.id,"caller_name":request.data["caller"]})
    if serializer.is_valid():
        serializer.save()
        return Response("Success")
    else:
        print(serializer.errors) 
        return Response("failed")   

@api_view(['POST'])
def delete_status(request):
    print(request.data)
    user_obj=customer.objects.get(username=request.data["user"])
    print(user_obj.id)
    status_obj=Status_model.objects.get(id=request.data["id_status"],user=user_obj.id)
    print(status_obj)
    status_obj.delete()
    return Response("success")

@api_view(['POST'])
def follow(request):
    followed_user=request.data['followed_user']  
    follower=request.data['follower'] 
    print(follower)
    print(followed_user)
    profile_inst=customer.objects.get(username=followed_user)
    print(profile_inst.id)
    print(request.data)
    kp={'followed_user':profile_inst.id,'follower':follower}
    my_inst=customer.objects.get(username=follower)
    serializer=FollowSerializer(data=kp)
    if serializer.is_valid():
        serializer.save()
        profile_inst.followers +=1
   
        profile_inst.save()
        my_inst.following +=1
        my_inst.save()
        print(serializer.data)
    else:
        print(serializer.errors)       

   
    

    return Response(serializer.data)

@api_view(['POST'])
def unfollow(request):
    username=request.data['username']
    me=request.data['me']

    unfollow_user=customer.objects.get(username=username)
    print(unfollow_user)
    unfollow_user.followers -= 1
    unfollow_user.save()
    my_inst=customer.objects.get(username=me)
    if my_inst.following >0:
        my_inst.following -=1
        my_inst.save()
    follow_delete=followers.objects.get(followed_user=unfollow_user.id,follower=me)
    follow_delete.delete()
    following_users=followers.objects.filter(follower=me)
    users=[]
    for i in following_users:
        
         users.append(i.followed_user.id)
        
    print(users,"array")    

    kp=customer.objects.filter(id__in=users) 
    new=[]
    for i in kp:
        new.append(i.username)  


    return Response(new)

@api_view(['POST'])
def followed_users(request):
    me=request.data['me']
    print(me)
   
    following_users=followers.objects.filter(follower=me)
    users=[]
    for i in following_users:
        
         users.append(i.followed_user.id)
        
    print(users,"array")    

    kp=customer.objects.filter(id__in=users) 
    new=[]
    for i in kp:
        new.append(i.username)  

    print(new,"usernames who are followed")    



    serializer=UserSerializer(kp,many=True)

    return Response(new)

@api_view(['POST'])
def likes_view(request): 
    me=request.data['me'] 
    print(me)
    created_at=request.data['post']
    post_inst=Posts.objects.get(created_at=created_at)
    print(post_inst)
    
 
    check_likes=Likes.objects.filter(user=me,post=post_inst.id)
    print(check_likes)

    kp={"user":me,"post":post_inst.id}
    if check_likes : 
        check_likes.delete()
        post_inst.likes_for_post -=1
        post_inst.save()
        print("fkjkjfd")
        return Response("already liked") 
        



            


    else:
        serializer=LikesSerializer(data=kp)
        if serializer.is_valid():
            serializer.save()
            post_inst.likes_for_post +=1
            post_inst.save()
            print(serializer.data)
            post_serializer=PostSerializer(post_inst,many=False)
            return Response(post_serializer.data) 
        else:
            print(serializer.errors) 
            return Response(serializer.errors) 
       

@api_view(['POST'])
def comments_view(request):
    comment=request.data['comment']
    created_at=request.data['post']
    me=request.data['me']
    post_inst=Posts.objects.get(created_at=created_at)
    me_inst=customer.objects.get(username=me)
    print(me_inst.profile_pic)
    print(me_inst.string_pic)
    if me_inst.profile_pic != "False":
        kr=me_inst.profile_pic
    else:
        kr=me_inst.string_pic
   
    print(kr)

    user_serializer=UserSerializer(me_inst,many=False)
    kp={"comment":comment,"post":post_inst.id,"user":me_inst.username,"prof":str(kr)}
    serializer=CommentSerializer(data=kp,partial=True)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        post_serializer=PostSerializer(post_inst)
        return Response({"comment":serializer.data,"comment_user":user_serializer.data,"post":post_serializer.data})
    else:
         print(serializer.errors ) 
         return Response("failed")   



@api_view(['POST']) 
def reply_view(request):
    comment_obj=   Comments.objects.get(comment=request.data['comment'])
    serializer=ReplySerializer(data={"user":request.data['comment'],"reply":request.data['reply'],"comment":comment_obj.id}) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)    
    else:
        print(serializer.errors)
        return Response("failed")    


@api_view(['POST'])
def status_view(request):
    print(request.data['status'])
    
    status_user=request.data['user']
    user_inst=customer.objects.get(username=status_user)

    kp={"status":request.data['status'],"user":user_inst.id} 
    print(kp)
    serializer=StatusSerializer(data=kp) 
    if serializer.is_valid():
        serializer.save()
        print(serializer.data) 
        return Response("status saved")
    else:
        print(serializer.errors)
        return Response("status save failed")


@api_view(['POST'])
def get_status_view(request):
    username=request.data["username"]
    print(username)
    cust_inst=customer.objects.get(username=username)
    serializer=UserSerializer(cust_inst,many=False)
    return Response(serializer.data)


       





    







        




   

