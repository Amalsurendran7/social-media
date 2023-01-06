from rest_framework import serializers 
from .models import *



class ReplySerializer(serializers.ModelSerializer):
    
    
 
    class Meta:
        model = reply
        fields = '__all__'  

class CommentSerializer(serializers.ModelSerializer):
    reply_of=ReplySerializer(many=True,read_only=True)
    
 
    class Meta:
        model = Comments
        fields = ('comment','user','post','prof','reply_of')  

class PostSerializer(serializers.ModelSerializer):
    comment_for=CommentSerializer(many=True,read_only=True)
 
    
    
 
    class Meta:
        model = Posts
        fields = ('file','created_at','likes_for_post','user','caption','comment_for')


class FollowSerializer(serializers.ModelSerializer):
    
    
 
    class Meta:
        model = followers
        fields = '__all__'  

       


class LikesSerializer(serializers.ModelSerializer):
    
    
 
    class Meta:
        model = Likes
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    
    
 
    class Meta:
        model = Status_model
        fields = '__all__'



class CallSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Calls_video
        fields = '__all__'
     







               
   