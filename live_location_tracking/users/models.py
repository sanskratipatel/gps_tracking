# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    # Modify the related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change related name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Change related name to avoid conflict
        blank=True
    )

    def __str__(self):
        return self.username
