from rest_framework import serializers 
from .models import *


class G_CommentSerializer(serializers.ModelSerializer):
    
    
 
    class Meta:
        model = G_Comments
        fields = ('comment','user','post','prof')  


class UserPostSerializer(serializers.ModelSerializer): 
     class Meta:
        model=post_user
        fields=['username','followers','following','profile_pic','string_pic','post']



class G_PostSerializer(serializers.ModelSerializer):
    comment_for=G_CommentSerializer(many=True,read_only=True)
    posted_by=UserPostSerializer(many=True,read_only=True)
    
 
    class Meta:
        model = G_Posts
        fields = ('file','created_at','likes_for_post','caption','comment_for','posted_by','group')


  


class G_LikesSerializer(serializers.ModelSerializer):
    
    
 
    class Meta:
        model = G_Likes
        fields = '__all__'




class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=group_members
        fields=['username','group']
     

class Group_Serializer(serializers.ModelSerializer): 
    post_to_group=G_PostSerializer(many=True,read_only=True)
    group_member=MemberSerializer(many=True,read_only=True)
    class Meta:
        model=Group_model
        fields=['group_name','description','post_to_group','admin','members_count','group_member']     





