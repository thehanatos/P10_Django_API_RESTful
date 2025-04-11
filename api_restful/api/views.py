from django.shortcuts import render

from rest_framework import viewsets
from .models import Project, Issue, Comment, Contributor
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import CustomUser

from .permissions import IsContributorOrAdmin, IsAuthorOrReadOnly, IsAuthorOrAdmin, IsAssigneeValid, IsContributorOrAdminProject
from rest_framework import permissions


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def get_queryset(self):
        return Project.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated(), IsContributorOrAdminProject()]
        return super().get_permissions()

class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    permission_classes = [IsAuthenticated, IsContributorOrAdmin, IsAuthorOrReadOnly, IsAuthorOrAdmin, IsAssigneeValid]
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Issue.objects.filter(project__id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        serializer.save(author=self.request.user, project_id=project_id)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsContributorOrAdmin, IsAuthorOrReadOnly, IsAuthorOrAdmin]
    
    def get_queryset(self):
        issue_id = self.kwargs.get('issue_pk')
        return Comment.objects.filter(issue__id=issue_id)

    def perform_create(self, serializer):
        issue_id = self.kwargs.get('issue_pk')
        serializer.save(author=self.request.user, issue_id=issue_id)

class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()
    permission_classes = [IsAuthenticated]



class UserViewSet(viewsets.ModelViewSet): 
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Only logged users can see the list