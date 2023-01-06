from rest_framework import serializers 
from .models import *
 
 
class CompanySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = company_info
        fields = '__all__'

               
    def create(self, validated_data):
        return company_info.objects.create(**validated_data)  

      

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save() 
    #     return instance              