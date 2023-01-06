
from  .views  import *
from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers  



 
urlpatterns = [
  
       path('create_post/', PostView.as_view() ),
        path('current_profile/', current_profile_view ),
         path('suggestion/', suggestion),
          path('follow/', follow),
          path('unfollow/', unfollow),
          path('followed_users/', followed_users),
          path('likes/', likes_view),
          path('comments/', comments_view),
             path('status/', status_view),
              path('repy/', reply_view),
               path('get_status/', get_status_view),
                path('del_status/', delete_status),
                     path('set_call_notify/', call_notify),
                     
          
         

   
]