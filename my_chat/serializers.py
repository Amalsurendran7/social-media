from rest_framework import serializers 
from my_chat.models import *



class MessageSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Messages
        fields = ['user','content','room_name']

class ChatSerializer(serializers.ModelSerializer):
    messages=MessageSerializer(many=True,read_only=True)
    class Meta:
        model = message_model
        fields = ['room','sender','receiver','id','messages']


      





