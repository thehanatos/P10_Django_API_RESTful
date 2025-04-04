from django.shortcuts import render

from rest_framework import viewsets
from .models import Project, Issue, Comment, Contributor
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]

class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()
    permission_classes = [IsAuthenticated]



# ViewSet for users
class UserViewSet(viewsets.ModelViewSet): 
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Only logged users can see the list