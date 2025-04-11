from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, IssueViewSet, CommentViewSet, ContributorViewSet, UserViewSet
from rest_framework_nested import routers

# router.register('projects', ProjectViewSet)
# router.register('issues', IssueViewSet)
# router.register('comments', CommentViewSet)

# urlpatterns = [
#     path('', include(router.urls)),  # router roots
# ]

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
projects_router = routers.NestedDefaultRouter(router, r'projects', lookup='project')
projects_router.register(r'issues', IssueViewSet, basename='project-issues')
issues_router = routers.NestedDefaultRouter(projects_router, r'issues', lookup='issue')
issues_router.register(r'comments', CommentViewSet, basename='issue-comments')

router.register(r'contributors', ContributorViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls + projects_router.urls + issues_router.urls