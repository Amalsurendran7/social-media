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

@api_view(['POST'])
def chat_list(request):
    serializer=ChatSerializer(data={"room":request.data["sender"],"sender":request.data["sender"],"receiver":request.data["receiver"]},partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response("success")
    else:
        print(serializer.errors)   
        return Response("failed")

# @api_view(['POST'])
# def  call_notify(request):




@api_view(['POST'])
def  get_chat_list(request):
     obj=message_model.objects.filter(room=request.data['me']) 
     if obj:  
      serializer=ChatSerializer(obj,many=True)
      return Response(serializer.data)
     else:
        obj_=message_model.objects.filter(receiver=request.data['me'])    
        serializer=ChatSerializer(obj_,many=True)
        return Response(serializer.data)
        
@api_view(['POST'])
def save_message(request):
    serializer=MessageSerializer(data={"user":request.data['sender'],"room_name":request.data['id'],"content":request.data['message']}) 
    if serializer.is_valid():
        serializer.save()  
        return Response("success")
    else:
        print(serializer.errors)   
        return Response("failed") 

@api_view(['POST'])
def get_message(request):
    msg_obj=Messages.objects.filter(room_name=request.data['id'])
    serializer=MessageSerializer(msg_obj,many=True)
    return Response(serializer.data)

        