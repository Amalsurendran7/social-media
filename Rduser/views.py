from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from .tasks import *

from rest_framework.decorators import api_view
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import jwt,datetime
from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponse
from django.core.mail import send_mail
from django.dispatch import receiver
from my_chat.models import *
from django.db.models.signals import post_save
import json
import uuid
# Create your views here.
 



class pos(APIView):

    def get(self,request):
        ft=customer.objects.all()
        
        ftt=UserSerializer(ft,many=True)
        return Response(ftt.data)

    def post(self,request):
        username=request.data["username"]
        email=request.data["email"]
        password=request.data["password"]
        user=customer.objects.filter(username=username).exists()
        kp={"username":request.data['username'],"email":request.data['email'],"phone":request.data['phone'],"password":request.data['password'],"profile_pic":request.data['file']}
        print(kp)
        if user :
            mess="user already exist"
            print("exists")
            return Response(mess)



         
         
        else:
            serializer=UserSerializer(data=kp,partial=True)

            if serializer.is_valid() :
                serializer.save()
              
            #   @receiver(post_save,sender=customer)
            #   def send_email(sender, **kwargs):
                # celery_email(email,username)
                subject = 'Email verification'
                myuuid = uuid.uuid4()
                print(email)
                
                message = "http://127.0.0.1:3000/thank/"+str(myuuid)+"/"+username
                email_from = 'amal76735@gmail.com'
                
                recipient_list=[email]
                
                send_mail( subject, message, email_from ,recipient_list)

                
                # refresh = RefreshToken.for_user(serializer.data)

                return Response(serializer.data)
        return Response({serializer.errors}) 

# def celery_email(email,username):
#     send_email_task.delay(email,username)


def send_email(email,username):

    subject = 'Email verification'
    myuuid = uuid.uuid4()
    
    
    message = "http://127.0.0.1:3000/thank/"+str(myuuid)+"/"+username
    email_from = 'amal76735@gmail.com'
    
    recipient_list=[email]
    
    send_mail( subject, message, email_from ,recipient_list)




@api_view(['GET','POST'])
def google(request):
  
   print(request.data)
   username=request.data["username"]
   email=request.data["email"]

       
   user=customer.objects.filter(username=username).exists()
   kp={"username":request.data['username'],"email":request.data['email'],"string_pic":request.data['pic']}
    
   print(kp)
   if user :
            mess="user already exist"
            print("exists")
            return Response(mess)



         
         
   else:
            serializer=UserSerializer(data=kp,partial=True)

            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else:
                print(serializer.errors)  
                return Response(serializer.errors)  

              


@api_view(['GET','POST'])
def validateEmailToken(request):

    token = request.data['id']
    username =request.data['username']
    print(username,"me")
    print(token,"token")
    t=customer.objects.all()
    print(t)
   
    
    
    if  token is not None:
        tokenExists = customer.objects.get(username=username)
        
        tokenExists.email_verified = True
        tokenExists.save()
           
        return Response("success") 

    else:
        res = {
            'status': 'failed',
            'message': 'Invalid',
        }
        return Response(res)       
         





class LogoutView(APIView):
    def get(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response



   
import os
import random
from twilio.rest import Client
@api_view(['POST','GET'])
def otp_send(request):
    phone=request.data["phone"]
    phone_number=customer.objects.filter(phone=phone)
    if phone_number:
    

        # account_sid = os.environ['ACCOUNT_SID']
        # auth_token = os.environ['AUTH_TOKEN']
        client = Client('AC8e0362d370ccfbd9eb24836063046750','f6910d11a24e02723cc95bca340e940a')
        otp=random.randint(1, 10000)
        for i in phone_number:
            i.otp=otp
            i.save() 
        
        message = client.messages .create(
                            body="Your otp code is"+str(otp),
                            from_='+16506634151',
                            to='+91'+phone
                        )

        print(message.sid)
        return Response("success")
    else:
        return Response("user not registered")   


@api_view(['POST'])
def otp_verify(request):
    otp=request.data['otp'] 
    # phone=request.data['phone']
    otp_obj=customer.objects.filter(otp=otp).values()
    print(otp_obj)
    # serializers=UserSerializer(otp_obj,many=False)
    if otp_obj:
        return Response({"message":"verified","serializer":otp_obj})  
    else:
        return Response({"message":"not verified"})    

    






@api_view(['POST','GET'])
def hello_world(request):
    username=request.data['username']
    password=request.data['pass']
    # check=customer.objects.filter(username=username,password=password)
    print(username,password)

    user = customer.objects.filter(username=username,password=password,email_verified=True).first()
    # check_email=customer.objects.filter(email_verified=False,username=username).first()
    
 

    if user is None:
        api_res="invalid credentials"
        return Response("invalid credentails")
        
    elif user:
        payload = {
            'id': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        

        response = Response()

        response.set_cookie(key='jwt',value= token,httponly=True)
        response.data = {
                'jwt': token
            }
        return response

    # elif check_email:
    #     return Response("Email not verified")          


                

 
    
       


    
 


        




@api_view(['POST','GET'])
def admin_api(request):
    username=request.data['u']
    password=request.data['p']
    print(username,password)
    check=authenticate(username=username,password=password)
    print(check)
    if check:
        api_res="true"
    else:
        api_res="false"    


    return Response(api_res) 

       

