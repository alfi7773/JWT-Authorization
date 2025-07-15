from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from api.serializers import CustomTokenObtainPairSerializer, LoginSerializer, ReadUserSerializer, RegisterSerializer
from users.models import MyUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    pass

class LoginApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email, password = serializer.validated_data.get('email'), serializer.validated_data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            read_serializer = ReadUserSerializer(user, context={'request': request})

            data = {
                **read_serializer.data,
                'token': token.key,
                'user': read_serializer.data
            }

            return Response(data)

        return Response({'detail': 'Пользователь не найден или не правильный пароль.'}, status=status.HTTP_400_BAD_REQUEST)



class RegisterView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {"message": "Пользователь создан",
             "user": user,
            },
            status=status.HTTP_201_CREATED
        )




# Create your views here.
