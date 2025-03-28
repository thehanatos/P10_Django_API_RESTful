from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login 
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission

class RedirectIfNotAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False

class DashboardView(APIView):
    permission_classes = [RedirectIfNotAuthenticated]

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/login/')  
        return Response({'message': 'asolkdhjasd!'})

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        print("coucou")
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("user is ok")
            return HttpResponseRedirect(redirect_to='/')
        print("user is none")
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

