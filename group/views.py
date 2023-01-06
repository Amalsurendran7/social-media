from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .seralizers import *
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


class GroupView(APIView):
    def get(self,request):
        group_obj=Group_model.objects.all()
        serializer=Group_Serializer(group_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
         admin=request.data['admin'] 
         group_name=request.data['group_name'] 
         desc=request.data['desc'] 
         cust_obj=customer.objects.get(username=admin)
         serializer=Group_Serializer(data={"group_name":group_name,"description":desc,"admin":admin},partial=True)
         
         if serializer.is_valid():
            serializer.save()
            group_obj=Group_model.objects.get(group_name=group_name)
            group_obj.user=cust_obj
            group_obj.save()
            m_serializer=MemberSerializer(data={"username":admin,"group":group_obj.id})
            if m_serializer.is_valid():
                m_serializer.save()
            
            return Response(serializer.data)
         
         else:
            return Response(serializer.errors)

@api_view(['POST'])
def join_group(request):
    me=request.data['me'] 
    group=request.data['group_name']
    group_obj=Group_model.objects.get(group_name=group)
    cust_obj=customer.objects.get(username=me)
    group_obj.user=cust_obj.id
    group_obj.members_count +=1
    group_obj.save()
    m_serializer=MemberSerializer(data={"username":me,"group":group_obj.id})
    if m_serializer.is_valid():
            m_serializer.save()
            return Response("success") 
    else:
        print(m_serializer.errors)
        return Response("sera")        


 
   
 
        
  



class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)
   
    def post(self, request, *args, **kwargs):
        print(request.data)
      
        me=request.data['user']
        group=request.data['group']
        print(group)
        customer_inst=customer.objects.get(username=me)
        group_obj=Group_model.objects.get(group_name=group)
        print(group_obj,"group to post")
        caption=request.data['caption']
        kp={"file":request.data['file'],"caption":request.data['caption'],"group":group_obj.id}
        print(kp)

        posts_serializer = G_PostSerializer(data=kp,partial=True)
        if posts_serializer.is_valid():
            posts_serializer.save()
            post_obj=G_Posts.objects.get(caption=request.data['caption'])
            print(post_obj,"mine")
            post_user_obj=UserPostSerializer(data={"username":customer_inst.username,"followers":customer_inst.followers,"following":customer_inst.following,"profile_pic":customer_inst.profile_pic,"string_pic":customer_inst.string_pic,"post":post_obj.id},partial=True)
            if post_user_obj.is_valid():
                post_user_obj.save()
            else:
                print(post_user_obj.errors)    
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)   





@api_view(['POST'])
def likes_view(request): 
    me=request.data['me'] 

    created_at=request.data['post']
    post_inst=G_Posts.objects.get(created_at=created_at)
    print(post_inst)
    
 
    check_likes=G_Likes.objects.filter(user=me,post=post_inst.id)
    print(check_likes)

    kp={"user":me,"post":post_inst.id}
    if check_likes : 
        check_likes.delete()
        post_inst.likes_for_post -=1
        post_inst.save()
        print("fkjkjfd")
        return Response("already liked") 
        



            


    else:
        serializer=G_LikesSerializer(data=kp)
        if serializer.is_valid():
            serializer.save()
            post_inst.likes_for_post +=1
            post_inst.save()
            print(serializer.data)
            post_serializer=G_PostSerializer(post_inst,many=False)
            return Response(post_serializer.data) 
        else:
            print(serializer.errors) 
            return Response(serializer.errors) 
       

@api_view(['POST'])
def comments_view(request):
    comment=request.data['comment']
    created_at=request.data['post']
    me=request.data['me']
    post_inst=G_Posts.objects.get(created_at=created_at)
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
    serializer=G_CommentSerializer(data=kp,partial=True)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        post_serializer=G_PostSerializer(post_inst)
        return Response({"comment":serializer.data,"comment_user":user_serializer.data,"post":post_serializer.data})
    else:
         print(serializer.errors ) 
         return Response("failed")   


@api_view(['POST'])
def get_group(request):
    group=request.data['group']   
    group_obj=Group_model.objects.get(group_name=group)   
    serializer= Group_Serializer(group_obj,many=False) 
    return Response(serializer.data)