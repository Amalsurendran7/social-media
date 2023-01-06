
from Rduser import views 
from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers  



 
urlpatterns = [
  
       path('hello_world/', views.hello_world ),
              path('register/', views.pos.as_view()),
                          path('admin_api/', views.admin_api),
                                path('google/', views.google),
                                 path('otp_send/', views.otp_send),
                                 path('otp_verify/', views.otp_verify),
                             path('verify_email_token/', views.validateEmailToken),
                              
            
    path('logout/',views.LogoutView.as_view()),
  

                
    #                   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
         

   
]