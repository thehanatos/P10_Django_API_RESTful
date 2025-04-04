from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, IssueViewSet, CommentViewSet, ContributorViewSet, UserViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('issues', IssueViewSet)
router.register('comments', CommentViewSet)
router.register('contributors', ContributorViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # router roots
]
