from rest_framework import permissions
from .models import Contributor, Project, Issue, Comment

class IsContributorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if view.basename == 'project':
            return True  
        project_id = request.parser_context['kwargs'].get('project_pk') or request.data.get('project')
        return Contributor.objects.filter(project_id=project_id, user=request.user).exists()
    
class IsContributorOrAdminProject(permissions.BasePermission):
    """
    Autorise uniquement les contributeurs du projet ou les admins à accéder au détail.
    """

    def has_object_permission(self, request, view, obj):
        # Admin a tous les droits
        if request.user.is_staff:
            return True
        
        # Vérifie si l'utilisateur est contributeur du projet
        return Contributor.objects.filter(project=obj, user=request.user).exists()

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class IsAssigneeValid(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST" and request.data.get('assignee'):
            project_id = request.data.get('project')
            assignee_id = request.data.get('assignee')
            return Contributor.objects.filter(user_id=assignee_id, project_id=project_id).exists()
        return True

class IsAuthorOrAdmin(permissions.BasePermission):
    """
    Autorise seulement l'auteur de l'objet ou un admin à modifier ou supprimer.
    Lecture autorisée pour tous les utilisateurs authentifiés.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff


class IsSelfOrAdmin(permissions.BasePermission):
    """
    Autorise uniquement l'utilisateur lui-même ou un admin à modifier/supprimer un user.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj or request.user.is_staff