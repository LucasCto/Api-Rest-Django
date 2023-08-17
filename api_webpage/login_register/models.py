from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string

# Create your models here.
class CustomUser(AbstractUser):
    # Definición del modelo CustomUser
    
    access_token = models.CharField(max_length=100, blank=True, null=True)
    
    # Agregar el argumento related_name para evitar el conflicto en los accesos inversos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.name