from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UsersSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegestrationView(APIView):
    def post(self, request):
        serialized = UsersSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create(username=serialized.data.get('username'), password=serialized.data.get('password'))
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            tokens = get_tokens_for_user(user)
            context = {
                'tokens': tokens,
                'message': 'login done'
            }
            return Response(context)
        return Response({'error: User not found'})
