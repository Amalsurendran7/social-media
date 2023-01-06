from rest_framework import serializers 
from .models import *
from home.serializers import PostSerializer,StatusSerializer,CallSerializer,FollowSerializer
from group.seralizers import *

 
class UserSerializer(serializers.ModelSerializer):
    post_by=PostSerializer(many=True,read_only=True)
    status_by=StatusSerializer(many=True,read_only=True)
    joined_group=Group_Serializer(many=True,read_only=True)
    group_post=G_PostSerializer(many=True,read_only=True)
    calls_for=CallSerializer(many=True,read_only=True)
    user_followed=FollowSerializer(many=True,read_only=True)
    class Meta:
        model = customer
        fields = ['username',
                  'email',
                  'phone',
                  'password','post_by','profile_pic','followers','following','user_followed','status_by','calls_for','string_pic','reported','joined_group','group_post','verified']

               
    def create(self, validated_data):
        return customer.objects.create(**validated_data)  

      

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save() 
    #     return instance              