from django.shortcuts import render

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
import jwt,datetime
from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponse
import json
# Create your 

# Create your views here.

class Company_Save(APIView):

    def post(self,request):

        company_name=request.data["company_name"]
        username=request.data['username']
        print(company_name)
        check_c_name=company_info.objects.filter(company_name=company_name).first()
        if check_c_name:
            return Response("company name already exists")
        else:

            serializer=CompanySerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response("succeessfull saved!!")
            else:
                return Response("serialzer validation failed")

    def get(self,request):
        company_list=company_info.objects.filter(processing=False)
        # company_list=company_info.objects.all()
        

        serializer=CompanySerializer(company_list,many=True)
        print(serializer.data)
            
        return Response(serializer.data)   


class Company_Pending(APIView) :

    def get(self,request):
        p_company=company_info.objects.filter(processing=True)
        serializer=CompanySerializer(p_company,many=True)
        return Response(serializer.data)

@api_view(['POST']) 
def declined(request):
    id=request.data['id']
    decline_company=company_info.objects.get(id=id)
    print(decline_company)
    decline_company.declined=True
    decline_company.save()

    declined=request.data['declined']
   
    example=[id,334,445]
   
    
    kp=[i   for i in declined if i['id'] not in example]
    
    d_company=company_info.objects.filter(declined=True)
    serializer=CompanySerializer(d_company,many=True)
      

    return Response({"pending":kp,"declined":serializer.data})


@api_view(['POST']) 
def Approved(request):
    print("data from",request.data['pending'])
    pending=request.data['pending']
    id=request.data['id']
    print(type(pending))
    print(pending)
    example=[id,334,445]
   
    
    kp=[i   for i in pending if i['id'] not in example]
    print("kp",kp)  
    
    
    approve_company=company_info.objects.get(id=id)
    print(approve_company)
    approve_company.is_pending=False
    approve_company.save()
    a_company=company_info.objects.filter(is_pending=False)
  
    serializer=CompanySerializer(a_company,many=True)
    # p_company=company_info.objects.filter(is_pending=True,processing=True)
    
    
    # serializers=CompanySerializer(p_company,many=True)
    return Response({"approved":serializer.data,"pending":kp})

    

     


@api_view(['GET']) 
def get_all(request):
    all_company=company_info.objects.all()
    serializer=CompanySerializer(all_company,many=True)
    return Response(serializer.data)
@api_view(['GET']) 
def process_C(request,id):
    decline_company=company_info.objects.get(id=id)
    print(decline_company)
    decline_company.processing=True
    decline_company.save()  

    # p_company=company_info.objects.filter(processing=True)
    serializer=CompanySerializer(decline_company,many=False)
    print(serializer.data)
    r_company=company_info.objects.filter(processing=False)
    serializers=CompanySerializer(r_company,many=True)

    return Response({"pending":serializer.data,"registered":serializers.data})

    
 
@api_view(['GET'])
def get_Approved(request):
        p_company=company_info.objects.filter(is_pending=False)
        serializer=CompanySerializer(p_company,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_pending(request):
        p_company=company_info.objects.filter(processing=True,declined=False,is_pending=True)
        serializer=CompanySerializer(p_company,many=True)
        return Response(serializer.data) 



@api_view(['GET'])
def get_declined(request):
        p_company=company_info.objects.filter(declined=True)
        serializer=CompanySerializer(p_company,many=True)
        return Response(serializer.data) 



@api_view(['POST'])
def booking(request): 
    select=request.data['select_value']
    print(request.data['slot'])
    dataa={key:value for key,value in request.data.items() if key != "select_value"}
    print(dataa)
    company_inst=company_info.objects.get(company_name=select)    
    serializer  =CompanySerializer(company_inst,data=dataa,partial=True) 
    if serializer.is_valid(): 
      serializer.save()
      print("success")
      return Response(serializer.data)
    return Response("failed")   

@api_view(['POST']) 
def Your_Company(request):
    username=request.data['username']
    print(username)
    company_row=company_info.objects.filter(username=username)
    if company_row:
       serializer=CompanySerializer(company_row,many=True)
       return Response(serializer.data)

    else:
           return Response("failed")




     

  






        
