from django.urls import path
from .views import *

urlpatterns = [
    
     path('chat_list/', chat_list),
     path('get_chat/',get_chat_list),
     path('save_message/', save_message),
     path('get_message/', get_message),
 


]
