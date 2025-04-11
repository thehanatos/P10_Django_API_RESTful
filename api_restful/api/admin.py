from django.contrib import admin

from .models import CustomUser, Project, Issue, Comment

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'age', 'can_be_contacted', 'can_data_be_shared']
    search_fields = ['username', 'email']
    list_filter = ['can_be_contacted', 'can_data_be_shared']
    


@admin.register(Project)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['description']