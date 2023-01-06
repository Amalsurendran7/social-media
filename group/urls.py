from  .views  import *
from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers  



 
urlpatterns = [
  
       path('create_group/', GroupView.as_view() ),
         path('join_group/',join_group ),
                  path('get_group/',get_group),
          path('g_likes/',likes_view ),
            path('g_comments/',comments_view),
          path('create_group_post/',PostView.as_view() ),



]
