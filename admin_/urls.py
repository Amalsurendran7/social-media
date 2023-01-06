from  .views  import *
from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers  



 
urlpatterns = [
  
       path('verification/', VerifyView.as_view() ),
        path('set_verify/', set_verify ),
             path('report/', reported.as_view()),
        
      
      
]
