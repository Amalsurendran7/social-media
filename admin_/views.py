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
class VerifyView(APIView):
    def get(self,request):
        cust_obj=customer.objects.filter(verify_request=True,verified=False)
        serializer=UserSerializer(cust_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        username=request.data['username']    
        cust_obj=customer.objects.get(username=username)
        cust_obj.verify_request=True
        cust_obj.save()
        return Response("success")


@api_view(['POST'])
def set_verify(request):
    username=request.data['username']
    print(username)
    cust_obj=customer.objects.get(username=username)
    cust_obj.verified=True
    cust_obj.save()
    print("yses")
    return Response("success")






 
class reported(APIView):
    def post(self,request): 
        username=request.data['username']  
        created_at=request.data['created_at']
        reason=request.data['reason']  
        cust_obj=customer.objects.get(username=username)
        cust_obj.reported=True
        cust_obj.save()
        post_obj=Posts.objects.get(created_at=created_at)
        post_obj.reported=True
        post_obj.reason=reason
        post_obj.save()
        return Response("ok")

    def get(self,request):
        cust_obj =customer.objects.filter(reported=True)  
        serializer=UserSerializer(cust_obj,many=True)  
        return Response(serializer.data)
        


