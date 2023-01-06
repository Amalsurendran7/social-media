from django.contrib import admin
from .models import *
from home.models import *


 
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','phone','password','email_verified','followers','following','online','string_pic']

admin.site.register(customer,UserAdmin) 




admin.site.register(Status_model)  

