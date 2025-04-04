from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.age is not None and self.age < 15:
            self.can_be_contacted = False
            self.can_data_be_shared = False
        super().save(*args, **kwargs)


class Contributor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    role = models.CharField(max_length=100)  # Ex: "Developer", "Manager"

    class Meta:
        unique_together = ('user', 'project')


class Project(models.Model):
    TYPE_CHOICES = [
        ('BACKEND', 'Back-end'),
        ('FRONTEND', 'Front-end'),
        ('IOS', 'iOS'),
        ('ANDROID', 'Android'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):
    PRIORITY_CHOICES = [('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')]
    TAG_CHOICES = [('BUG', 'Bug'), ('FEATURE', 'Feature'), ('TASK', 'Task')]
    STATUS_CHOICES = [('TODO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('FINISHED', 'Finished')]

    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assignee = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_issues')
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10, default='LOW')
    tag = models.CharField(choices=TAG_CHOICES, max_length=10, default='TASK')
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default='TODO')
    created_time = models.DateTimeField(auto_now_add=True)


import uuid

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
