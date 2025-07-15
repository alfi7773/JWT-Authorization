from users.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




User = get_user_model()


class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id','username', 'email', ]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):
    



    class Meta:
        model = MyUser   
        # fields = '__all__'
        fields = ['id','username', 'email', 'password', ] 




    

    def create(self, validated_data):
        user = MyUser.objects.create_user (
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        # print(user)
        return ReadUserSerializer(user).data
    
    
class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    
