
from company import views 
from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers  



 
urlpatterns = [
     path('company_save', views.Company_Save.as_view() ),
      path('company_pending', views.Company_Pending.as_view() ),
            path('decline/', views.declined ),
             path('approve/', views.Approved ),
                  path('process/<int:id>', views.process_C),
                    path('get_approved', views.get_Approved),
                       path('get_pending', views.get_pending),
                       path('get_declined', views.get_declined),
                    path('get_all', views.get_all),
                    path('booking', views.booking),
                        path('your_company/', views.Your_Company),
     

   
]