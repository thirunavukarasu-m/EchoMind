from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('tester', 'tester'),
        ('user', 'User')
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=6, choices=ROLES)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

