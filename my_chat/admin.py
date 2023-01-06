from django.contrib import admin
from .models import *

# Register your models here.
class Message_modelAdmin(admin.ModelAdmin):
    list_display = ['room','sender','receiver']

admin.site.register(message_model,Message_modelAdmin) 

class MessageAdmin(admin.ModelAdmin):
    list_display=['user','content','room_name']


admin.site.register(Messages,MessageAdmin)
