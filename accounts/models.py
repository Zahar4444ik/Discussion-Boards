from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set', verbose_name='groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set',
                                              verbose_name='user permissions')